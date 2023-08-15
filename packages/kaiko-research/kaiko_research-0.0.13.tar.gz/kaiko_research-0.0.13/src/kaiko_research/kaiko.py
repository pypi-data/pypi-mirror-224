from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import importlib
from kaiko_research.api_client import DataAPIClient
from kaiko_research.endpoint_schemas import endpoints_mapping, api_wrapper_params
from kaiko_research.utils import check_dates, convert_to_date_string, compare_dates
api_wrapper_params = pd.DataFrame(api_wrapper_params)
endpoints_mapping = pd.DataFrame(endpoints_mapping)


class KaikoAPIWrapper:
    def __init__(self, api_key):
        print("Dear user, thank you for installing Kaiko API wrapper!\nThere are the three methods that you could use:\n1. get_enpoints_information(), which will give you the list of Kaiko endpoints with the description of each\n2. get_export_parameters(endpoint_name), which will indicate to you the parameters that you can enter for fetching the data\n3. get_data(params), which will help you to fetch data from Kaiko API\n\n We hope that you will enjoy using it! Should you have any questions feel free to contact: evgeny.ryabchenkov@kaiko.com\n")
        self.api_key = api_key

    def get_enpoints_information(self):
        msg = "You have requested a Dataframe containing a comprehensive list of endpoints, with their respective classifications and descriptions. To request values from the Kaiko API using the wrapper, please refer to the endpoint names provided within this list. For a more in-depth understanding of these endpoints, please refer to the https://docs.kaiko.com/."
        print(msg)
        return endpoints_mapping[["endpoint_name", "data_type", "description"]]

    def get_endpoint_parameters(self, endpoint_name):
        if (endpoint_name) not in endpoints_mapping['endpoint_name'].tolist():
            print(
                f"Sorry the endpoint '{endpoint_name}' does not exist or is not currently supported by the API wrapper")
            return pd.DataFrame()
        elif (endpoint_name in ['Assets', 'Exchanges']):
            print(
                f"There are no parameters required for '{endpoint_name}' endpoint")
            return pd.DataFrame()
        elif (endpoint_name in ['Instruments', 'Pools']):
            print(
                f"API wrapper does not support parameters for '{endpoint_name}' endpoint")
            return pd.DataFrame()

        msg = f"You have requested a Dataframe with a list of API wrapper parameters for {endpoint_name}.\n\nPlease note that API wrapper parameters can have a different format than those in Kaiko API docs"
        print(msg)
        schemas = importlib.import_module("endpoint_schemas")
        schema_name = [
            _["schema_name"] for i, _ in endpoints_mapping.iterrows() if _["endpoint_name"] == endpoint_name
        ][0]
        schema = getattr(schemas, schema_name)

        endpoint_params = api_wrapper_params.loc[api_wrapper_params[endpoint_name]
                                                 != "-"].reset_index(drop=True)
        the_list_of_not_query = [
            k for k, v in schema.items() if not v['part_of_query']]

        endpoint_params = endpoint_params[~endpoint_params['parameter'].isin(
            the_list_of_not_query + ['continuation_token'])]

        the_list_of_related_fields = [
            x for _ in endpoint_params[endpoint_name] for x in str(_).split(',')]

        endpoint_specific = [k for k, v in schema.items() if v['part_of_query'] and k !=
                             'continuation_token' and k not in the_list_of_related_fields]

        for pm in endpoint_specific:
            pm_obj = {}
            pm_obj['parameter'] = pm
            pm_obj['type'] = schema[pm]['type']
            pm_obj['required'] = schema[pm]['required']
            try:
                pm_obj['default'] = schema[pm]['default']
            except:
                pass
            pm_obj['parameter_comment'] = f"specific for '{endpoint_name}' endpoint, please check detailed documentation on https://docs.kaiko.com/"
            pm_df = pd.Series(pm_obj).to_frame().T.astype(
                {"parameter": str, "type": str, 'required': bool, 'parameter_comment': str})
            endpoint_params = pd.concat(
                [endpoint_params, pm_df], ignore_index=True)

        return endpoint_params[['parameter', 'type', 'required', 'default', 'parameter_comment']]

    def get_data(self, **kwargs):
        api_client = DataAPIClient(self.api_key)
        data = {}
        endpoint_name = kwargs.get('endpoint_name')
        if (not endpoint_name):
            print('Please specify the name of endpoint')
            return data
        elif (endpoint_name) not in endpoints_mapping['endpoint_name'].tolist():
            print(
                f"Sorry the endpoint '{endpoint_name}' does not exist or is not currently supported by the API wrapper")
            return data

        # Constructing the parameters
        if (endpoint_name not in ['Assets', 'Exchanges', 'Instruments', 'Pools']):
            params_template = self.get_export_parameters(endpoint_name)
            params_template = params_template.set_index('parameter')
            fields = api_wrapper_params.loc[api_wrapper_params['parameter'].isin(
                params_template.index.tolist())][['parameter', endpoint_name, 'ref_data', 'required']].set_index('parameter')
            param_constructor = {}
            fields_provided = fields.loc[fields.index.isin(kwargs.keys())]
            for p in kwargs.keys():
                if (p not in params_template.index.tolist()):
                    print(
                        f'Parameter "{p}" is not relevant for the endpoint "{endpoint_name}"')
            for i, p in params_template.iterrows():
                param = kwargs.get(i)
                param_constructor[i] = param

            if "period" in params_template.index.tolist():
                today = datetime.today().date()
                end_time = convert_to_date_string(today)
                one_month_earlier = today - relativedelta(months=1)
                start_time = convert_to_date_string(one_month_earlier)
                period = kwargs.get('period')
                if period:
                    period_length = len(period)

                    if any(not check_dates(p) for p in period):
                        return data
                    elif period_length == 1:
                        if not check_dates(period[0]):
                            return data
                        start_time = convert_to_date_string(period[0])
                    elif period_length == 2:
                        if not check_dates(period[0]) or not check_dates(period[1]):
                            return data
                        elif not compare_dates(period[0], period[1]):
                            return data
                        start_time = convert_to_date_string(period[0])
                        end_time = convert_to_date_string(period[1])
                    else:
                        print("Too many values for period")
                        return data

        # +++++++ PROCESS REFERENCE DATA +++++++
            inst_url = api_client.treat_request_data('Instruments')
            ref_data_params_present = fields_provided.loc[fields_provided['ref_data'] != ""].index.tolist(
            )
            insruments_params_present = fields_provided.loc[fields_provided['ref_data'] != "", 'ref_data'].tolist(
            )
            insruments_params = fields.loc[fields['ref_data']
                                           != "", 'ref_data']
            ep_instruments_params = fields.loc[fields['ref_data']
                                               != "", endpoint_name]
            ep_instruments_params = list(set(ep_instruments_params))
            ep_instruments_params_ep = [
                _.split(',')[0] for _ in ep_instruments_params]
            ep_instruments_params_inst = [
                _.split(',')[1] for _ in ep_instruments_params]
            if (len(insruments_params) > 0):
                instruments_data = api_client.fetch_raw_data(inst_url)
                instruments = instruments_data[insruments_params].drop_duplicates(
                )
                if (len(ref_data_params_present) > 0):

                    list_rel_params = api_client.combine_lists_of_params(
                        ref_data_params_present, [param_constructor[_] for _ in ref_data_params_present])
                    list_rel_params = pd.DataFrame(list_rel_params)
                    list_rel_params['test_field'] = list_rel_params.apply(
                        lambda row: '-'.join(map(str, row)), axis=1)
                    test_instruments = instruments_data[insruments_params_present]
                    test_instruments['test_field'] = test_instruments.apply(
                        lambda row: '-'.join(map(str, row)), axis=1)
                    instruments_data['test_field'] = test_instruments['test_field']

                    instruments = instruments_data.loc[instruments_data['test_field'].isin(
                        list_rel_params['test_field'].tolist()), ep_instruments_params_inst].drop_duplicates()
                instruments.columns = ep_instruments_params_ep
                fin_params = instruments.copy()
            elif ('pools' in params_template.index.tolist()):
                pools = kwargs.get('pools')
                if (pools):
                    fin_params = pd.DataFrame(pools)
                    fin_params.columns = ['pool_address']
                else:
                    pools_ulr = api_client.treat_request_data('Pools')
                    pools_data = api_client.fetch_raw_data(pools_ulr)
                    fin_params = pools_data[['address']].drop_duplicates()
                    fin_params.columns = ['pool_address']
            # return fin_params
        # +++++++ REQUEST ENDPOINT DATA +++++++
            # return fin_params
            if "period" in params_template.index.tolist():
                date_labels = fields.at['period', endpoint_name].split(',')
                fin_params[date_labels[0]] = start_time
                fin_params[date_labels[1]] = end_time
            if any([_ in kwargs.keys() for _ in params_template.index]):
                for _ in params_template.index:
                    if (_ not in ref_data_params_present + ['multiprocessing', 'usd_conversion', 'endpoint_name']):
                        try:
                            fin_params[_] = kwargs[_]
                        except:
                            pass

            fin_params = fin_params.to_dict(orient='records')
            # return fin_params
            multiprocessing = kwargs.get('multiprocessing')
            if (not multiprocessing):
                multiprocessing = False
            batch = kwargs.get('batch_size')
            if (not batch):
                batch = 10
            data = api_client.fetch_data_batches(
                endpoint_name, fin_params, multiprocessing, batch)
            return data
        else:
            url = api_client.treat_request_data(endpoint_name)
            data = api_client.fetch_raw_data(url)

        # +++++++ POSTPROCESS ENDPOINT DATA +++++++

        return data
