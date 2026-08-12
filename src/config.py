"""fastF1 cache manager"""

import os
import fastf1

from src.utils.settings import get_settings

def enable_cache():
	# Get cache location from settings
	settings = get_settings()
	cache_path = settings.cache_location

	# Check if cache folder exists
	if not os.path.exists(cache_path):
		os.makedirs(cache_path)

	# Enable local cache
	fastf1.Cache.enable_cache(cache_path)