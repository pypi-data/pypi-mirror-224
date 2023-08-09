from michaelPanThematicLib.draw_thematic_map_pillow import draw_thematic_by_pillow


input_dict = {
	"input_path": r'D:/pycharm_project/thematicMapTile/input_images/FY3D_MERSI_L3_LST_AVE_GLL_20230501000000_20230531235959_025KM_POAM_X_Global_X.png',
	"font_path": 'static/Helvetica-Neue-2.ttf',
	'satellite_sensor': 'FY3D/MERSI',
	'location1': 'global',
	'box': [-30, 330, -90, 90],
	'template_path_size_location': [r"D:/pycharm_project/thematicMapTile/static/world/global-L.png", 3600, 1800, 130, 272],
	'title_loc_size': [1400, 80, 100],
	'subtitle_loc_size': [3400, 200, 50],
	'legend_sat_loc_size': [2830, 2215, 2710, 2300, 50],
	'is_need_small': [0.5, 0.5, True],
	'prod_title': {"LST": {"title": "Land Surface Temperature", "D": "Land Surface Temperature(Day)"}},
	"color_bar_loc_filename": [53, 2300, "D:/pycharm_project/thematicMapTile/static/world/NDVI-cn1.png"],
}


a_image_list = draw_thematic_by_pillow(input_dict)
a_image_list[0].show()










