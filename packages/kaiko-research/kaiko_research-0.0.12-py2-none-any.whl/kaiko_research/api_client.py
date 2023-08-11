#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:39:58 2023

@author: evgenijrabcenkov
"""
from kaiko_research.request_handler import ReqUrlHandler
import itertools
import dask.bag as db
from tqdm import tqdm
import pandas as pd
import requests
FIELDS_WITH_LISTS = [
    "instrument",
    "exchange",
    "asset",
    "base_asset",
    "quote_asset",
    "instrument_class",
    "pool_address"
]


class DataAPIClient:
    def __init__(self, api_key):
        self.api = api_key
        self.req_handler = ReqUrlHandler()
        self.headers = self.req_handler.define_headers(api_key)

    # General functions to process request parameters and response
    def treat_request_data(self, endpoint, params={}):
        return self.req_handler.construct_url(endpoint, params)

    def combine_lists_of_params(self, fields, lists_of_params):
        product_lists_of_params = itertools.product(*lists_of_params)
        final_list = []
        for product in product_lists_of_params:
            obj = {}
            for i, item in enumerate(product):
                obj[fields[i]] = item
            final_list.append(obj)
        return final_list

    def fetch_raw_data(self, url, params={}):
        response = requests.get(url, headers=self.headers).json()
        data_res = pd.DataFrame()
        try:
            if (response['result'] == 'success'):
                res_data = response["data"]
                while (response.get("next_url") is not None) & (response["data"] != []):
                    response = requests.get(
                        response["next_url"], headers=self.headers).json()
                    res_data = res_data + response["data"]
                try:
                    data_res = pd.DataFrame(res_data)
                    for item in FIELDS_WITH_LISTS:
                        if item in params.keys():
                            data_res[item] = params[item]
                except ValueError as ve:
                    print(
                        f"error in generating dataset {ve} the response that you are getting:"
                    )
        except:
            print(response)
            pass
        return data_res

    def fetch_data_batches(self, endpoint, list_of_parameters, multiprocessing, batch_size=10):
        urls = []
        data = pd.DataFrame()
        if (multiprocessing):
            for param in tqdm(list_of_parameters, "Generating URLs..."):
                url = []
                self.url = self.treat_request_data(endpoint, param)
                url += [self.url]
                url += [param.copy()]
                urls.append(url)
            chunks = [urls[i: i + batch_size]
                      for i in range(0, len(urls), batch_size)]
            for i, chunk in enumerate(tqdm(chunks, "Fetching data in batches...")):
                bag = db.from_sequence([(url[0], url[1]) for url in chunk]).map(
                    lambda x: self.fetch_raw_data(*x)
                )
                try:
                    data_chunk = bag.compute()
                    data_chunk = pd.concat(data_chunk).reset_index(drop=True)
                except Exception as e:
                    print(f"Error occurred while fetching data: {e}")
                    return pd.DataFrame()
                data = pd.concat([data, data_chunk]).reset_index(drop=True)
        else:
            for param in tqdm(list_of_parameters, "Fetching data..."):
                url = self.treat_request_data(endpoint, param)
                data_piece = self.fetch_raw_data(url, param)
                data = pd.concat([data, data_piece]).reset_index(drop=True)
        return data
