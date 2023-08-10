#!/usr/bin/env python

import glob
import json
import os
import pandas as pd

from collector.utils import (
    remove_duplicates,
    remove_elements_with_keywords,
    save_data,
    select_elements_with_keywords
)


def filter_urls(new_urls):
    """Filters the urls to collect.

    Args:
        new_urls: list, list of dictionaries with the new urls.

    Returns:
        urls_to_collect: list, list of dictionaries with the new urls to collect with the status key 'collected' as no.
    """

    print("[LOG] Start the filtration of the urls.")

    urls_to_collect = []
    for new_url in new_urls:
        urls_to_collect.append({
            'url': new_url['url'],
            'category': new_url['category'],
            'sub_category': new_url['sub_category'],
            'sub_sub_category': new_url['sub_sub_category'],
            'collected': 'no'
        })

    print("[LOG] The filtration of the urls is finished.")
    print("[LOG] There are {} urls to collect.".format(len(urls_to_collect)))

    return urls_to_collect

def select_specific_urls(aggegated_urls, brands):
    """Selects specific urls with the products of the `brands`.

    Args:
        aggegated_urls: list, list of dictionaries of aggregated urls.
        brands: list, list of brands in lower case without any accents.
    
    Returns:
        specific_urls: list, list of dictionaries of specific aggregated urls.
    """

    specific_urls = []

    # Checks if the brand name is inside the url or the product name.
    for aggregated_url in aggegated_urls:
        for brand in brands:
            if brand in aggregated_url['product_name'].lower():  # TODO: transformer la valeur du str pour ne pas prendre en compte les accents
                specific_urls.append(aggregated_url)
            if brand in aggregated_url['product_brand'].lower():  # TODO: transformer la valeur du str pour ne pas prendre en compte les accents
                specific_urls.append(aggregated_url)
            if brand in aggregated_url['url'].lower():
                specific_urls.append(aggregated_url)

    # Remove the duplicates
    df = pd.DataFrame(specific_urls)
    df = df.drop_duplicates(subset=['url'], keep='first')
    df = df[['category', 'sub_category', 'sub_sub_category', 'url']]
    df = df.reset_index(drop=True)
    unique_aggregated_urls = df.to_dict(orient='records')
    
    return unique_aggregated_urls


def filter_specific_urls(specific_urls):
    """Filters the specific urls to collect.

    Args:
        specific_urls: list, list of dictionaries with the specific urls.

    Returns:
        urls_to_collect: list, list of dictionaries with the new urls to collect with the status key 'collected' as no.
    """

    print("[LOG] Start the filtration of the urls.")

    urls_to_collect = []
    for new_url in specific_urls:
        urls_to_collect.append({
            'url': new_url['url'],
            'category': new_url['category'],
            'sub_category': new_url['sub_category'],
            'sub_sub_category': new_url['sub_category'],
            'collected': 'no'
        })

    print("[LOG] The filtration of the urls is finished.")
    print("[LOG] There are {} urls to collect.".format(len(urls_to_collect)))

    return urls_to_collect


def filter_urls(source_dict, 
                keywords_for_removing, keywords_for_selecting,
                new_urls_folder_path, filtered_urls_folder_path):
    """Aggregates new URLs in 'aggregated_urls' folder and filters new URLs in 
    'filtered_urls' folder.

    Args:
        source_dict (dict): dictionary with information from the source.
        keywords_for_removing (list): list of keywords. 
        keywords_for_selecting (list): list of keywords.
        new_urls_folder_path (str): path to the 'new_urls' folder.
        filtered_urls_folder_path (str): path to the 'filtered_urls' folder.
    """

    # Load and aggregate the new URLs
    new_urls_dicts = []
    for new_url_dicts_file in glob.glob(os.path.join(new_urls_folder_path, '*.json')):
        for new_url_dict in json.load(open(new_url_dicts_file, 'r', encoding='utf8')):
            new_urls_dicts.append(new_url_dict)

    # Filter the new URLs
    # Remove the duplicates
    filtered_urls_dicts = remove_duplicates(dicts=new_urls_dicts, 
                                            key='url')
    # Remove the elements with specific keywords
    if keywords_for_removing:
        filtered_urls_dicts = remove_elements_with_keywords(dicts=filtered_urls_dicts, 
                                                            keys=['product_name', 'url'], 
                                                            keywords=keywords_for_removing)
    # Select the elements with specific keywords
    if keywords_for_selecting:
        filtered_urls_dicts = select_elements_with_keywords(dicts=filtered_urls_dicts, 
                                                            keys=['product_name', 'url'], 
                                                            keywords=keywords_for_selecting)
    # Remove the duplicates
    filtered_urls_dicts = remove_duplicates(dicts=filtered_urls_dicts, 
                                            key='url')

    # Save filtered URLs in 'filtered_urls' folder
    save_data(data=filtered_urls_dicts,
              saved_data_type='filtered_urls',
              source=source_dict['source'],
              path=filtered_urls_folder_path)
    print(f"[LOG] {len(filtered_urls_dicts)} filtered URLs have been saved in 'filtered_urls' folder.")