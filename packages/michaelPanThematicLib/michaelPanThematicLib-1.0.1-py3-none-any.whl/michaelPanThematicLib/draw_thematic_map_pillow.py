# ***************************************************************
# Copyright (c) 2023 shinetek. All Rights Reserved
# 此代码只能调用使用，未经本人(pct)或者公司(shinetek)许可，任何人不得复制、修改此代码。
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2023.8
# ***************************************************************
import os
import re
import time
import numpy as np
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont
from PIL import __version__ as pillow_version
from michaelPanPrintLib.change_print import print_with_style
"""
    这个公共库为对已有绘制专题图程序的改写与封装，旨在以最少的配置、最大的便捷性完成专题图的绘制。
    注：这个库的所有权归本人和华云星地通科技有限公司所有
"""

class ThematicParam(BaseModel):
    # ====================================================需要添加的内容==================================================
    input_path: str  # 主图输入路径
    font_path: str  # 字体路径
    satellite_sensor: str  # 星标和仪器名称
    location1: str  # 区域位置
    box: list  # 图像的边界框
    template_path_size_location: list  # 模板文件路径、尺寸、大小和位置
    title_loc_size: list  # 标题的内容、位置(x,y坐标)和大小,为大小为0时不添加该项
    subtitle_loc_size: list  # 副标题的内容、位置(x,y坐标)和大小,为大小为0时不添加该项
    legend_sat_loc_size: list  # 星标的位置(x,y坐标)、仪器的位置(x,y坐标)和字体大小
    is_need_small: list  # x、y的缩放比率和是否需要缩放开关，例子：[0.5, 0.5, True]
    prod_title: dict  # 例子：{"LST": {"title": "Land Surface Temperature", "D": "Land Surface Temperature(Day)"}}
    # ==================================================================================================================
    # ===================================================可以不添加的内容==================================================
    color_bar_loc_filename: list=[]  # 颜色条的位置(x,y坐标)和颜色条路径,为空时不添加该项
    logo_loc_filename: list=[]  # logo的位置和logo路径,为空时不添加该项
    legend_country_loc_filename: list=[]  # 图例国家的位置(x,y坐标)和路径,为空时不添加该项
    legend_uncountry_loc_filename: list = []  # 图例未定国界的位置(x,y坐标)和路径,为空时不添加该项
    legend_sea_loc_filename: list = []  # 图例海洋的位置(x,y坐标)和路径,为空时不添加该项
    legend_land_loc_filename: list = []  # 图例陆地的位置(x,y坐标)和路径,为空时不添加该项
    is_need_border: bool=True
    # ==================================================================================================================
    

def draw_thematic_by_pillow(input_dic):
    """
    :param input_dic: a dictionary that contain draw param
    :return: a list that contain thematic picture
    TODO:
        1.随着需求的变化而更新维护
        2.bug测试
        
    an example are as follows:
        from michaelPanThematicLib.draw_thematic_map_pillow import draw_thematic_by_pillow
        
        input_dict = {
            "input_path": 'test1/FY3D_MERSI_L3_LST_AVE_GLL_20230501000000_20230531235959_025KM_POAM_X_Global_X.png',
        
            "font_path": 'test1/Helvetica-Neue-2.ttf',
        
            'satellite_sensor': 'FY3D/MERSI',
            
            'location1': 'global',
            
            'box': [-30, 330, -90, 90],
            
            'template_path_size_location': ["test1/global-L.png", 3600, 1800, 130, 272],
            
            'title_loc_size': [1400, 80, 100],
            
            'subtitle_loc_size': [3400, 200, 50],
            
            'legend_sat_loc_size': [2830, 2215, 2710, 2300, 50],
            
            'is_need_small': [0.5, 0.5, True],
            
            'prod_title': {"LST": {"title": "Land Surface Temperature", "D": "Land Surface Temperature(Day)"}}
            }
        a_image_list = draw_thematic_by_pillow(input_dict)
        
        a_image_list[0].show()
    """
    t1 = time.time()
    thematic_param = ThematicParam(**input_dic)
    print_with_style(f'当前pillow库的版本为：{pillow_version}', color='cyan')
    # ****************************************************传入参数****************************************************
    file_path = thematic_param.input_path
    satellite_sensor = thematic_param.satellite_sensor
    location1 = thematic_param.location1
    box = thematic_param.box
    title_loc_size = thematic_param.title_loc_size
    subtitle_loc_size = thematic_param.subtitle_loc_size
    color_bar_loc_filename = thematic_param.color_bar_loc_filename
    logo_loc_filename = thematic_param.logo_loc_filename
    legend_sat_loc_size = thematic_param.legend_sat_loc_size
    font_path = thematic_param.font_path
    template_path_size_location = thematic_param.template_path_size_location
    legend_country_loc_filename = thematic_param.legend_country_loc_filename
    legend_province_loc_filename = thematic_param.legend_uncountry_loc_filename
    legend_sea_loc_filename = thematic_param.legend_sea_loc_filename
    legend_land_loc_filename = thematic_param.legend_land_loc_filename
    is_need_border = thematic_param.is_need_border
    is_need_small = thematic_param.is_need_small
    prod_title = thematic_param.prod_title
    # **************************************************************************************************************
    # *************************************输出文件名模块***********************************
    staid = os.path.basename(file_path).split('_')[0]
    prod_name = os.path.basename(file_path).split('_')[3]
    color_name = os.path.basename(file_path).split('_')[4]
    proj1 = os.path.basename(file_path).split('_')[5]
    res = os.path.basename(file_path).split('_')[8]
    time1 = os.path.basename(file_path).split('_')[6]  # 开始时间
    time2 = os.path.basename(file_path).split('_')[7]  # 结束时间
    orbits = os.path.basename(file_path).split('_')[10]
    # ***********************分辨率转换*********************
    pattern = r'\d+|[a-zA-Z]+'
    result = re.findall(pattern, res)
    res_num = int(result[0])
    result_unit = result[1].upper()
    reference_dictionary = {
        'M': 0.00001,
        'KM': 0.01
    }
    res1 = res_num * reference_dictionary[result_unit]
    # KM --> M
    if proj1 == "GLL":  # 等经纬的情况
        res = f"{res1}°"
    else:
        res = f"{res_num * 1000}m"
    # ****************************************************
    if len(prod_title[prod_name].keys()) <= 1 or color_name == 'NULL':  # 没有子标题的情况
        title1 = prod_title[prod_name]["title"]
    else:
        if color_name not in prod_title[prod_name].keys():
            print_with_style(f"子产品名对应的标题未找到，使用产品名{prod_title[prod_name]['title']}")
            title1 = prod_title[prod_name]["title"]
        else:
            title1 = prod_title[prod_name][color_name]  # 使用子产品名
    # 升降轨名称转换
    if orbits == "N" or orbits == "A":
        orbits = "Ascend"
    elif orbits == "D":
        orbits = "Descend"
    # **********************************************************************************
    img2 = Image.open(file_path)
    extend_list = ["SIP", "SIC", "SWS"]  # 排除列表
    if location1 == "Arab":  # 增加对阿拉伯地区主图尺寸过小的支持
        extend_list.append("OVW")
        img2 = img2.resize((template_path_size_location[1], template_path_size_location[2]))
    # ---------------------------------------------边界线处理--------------------------------------------------------
    if prod_name in extend_list:  # 去掉特殊情况
        print_with_style(f"跳过产品列表为:{extend_list}")
        print_with_style(f"绘图时跳过该产品({prod_name})边界线叠加")
    else:
        if is_need_border:
            img_border = Image.open(f'{os.path.dirname(os.path.abspath(__file__))}/static/global_-180_180.png')
            if location1.lower() == 'global':
                img_border = transform_image_coordinates(img_border, box)
            else:
                img_border = crop_image_by_bbox(img_border, box)
            img2.paste(img_border, (0, 0), mask=img_border)
            print_with_style(f"叠加边界线，范围是：{box[:4]}", color='blue')
        else:
            print_with_style(f"绘图时跳过边界线叠加")
    # ---------------------------------------------------------------------------------------------------------------
    # *************************************使用模板文件绘图，绘图第二方法*********************************************
    img_template = Image.open(template_path_size_location[0])
    img2 = img2.resize((template_path_size_location[1], template_path_size_location[2]))
    print_with_style(f"模板文件的尺寸为{img_template.size}, 主图的尺寸为：{img2.size}", color='blue')
    if img2.size[0] == img_template.size[0] and img2.size[1] == img_template.size[1]:
        print_with_style(f"模板尺寸与主图尺寸一致，使用内置模板策略", color='cyan')
        # 判断是否绘制云图，交换叠图顺序
        img_temp = img2
        img2 = img_template
        img_template = img_temp
        font_color = (255, 255, 255)
        img_template.paste(img2, (template_path_size_location[3], template_path_size_location[4]), mask=img2)  # 如果出错去掉mask
        # 创建绘图对象
        draw = ImageDraw.Draw(img_template)
        # **********************添加标题************************
        # 设置标题字体
        font_title = ImageFont.truetype(f'{font_path}', size=title_loc_size[2])
        if orbits != "X":
            title1 += f"({orbits})"
        if int(pillow_version.split('.')[0]) < 10:  # pillow版本大于10时，使用新版api
            title_text_width, title_text_height = draw.textsize(title1, font_title)
        else:
            x1_title, y1_title, x2_title, y2_title = font_title.getbbox(title1)
            title_text_width = abs(x2_title - x1_title)
            title_text_height = abs(y2_title - y1_title)
        x_title = (img_template.width - title_text_width) / 2
        text_border(draw, x_title, 0, title1, font_title, (0, 0, 0), font_color, location1)  # 绘制文字
        # **********************添加副标题************************
        # 设置副标题字体
        font_subtitle = ImageFont.truetype(f'{font_path}', size=subtitle_loc_size[2])
        # 添加副标题, 增加对月数据和天数据的区别
        subtitle_time = f"{time1[:4]}-{time1[4:6]}-{time1[6:8]} {time1[8:10]}:{time1[10:12]}(UTC)"
        # 新版库api在服务器上会出错，留存
        if int(pillow_version.split('.')[0]) < 10:  # pillow版本大于10时，使用新版api
            subtitle_text_width, _ = draw.textsize(subtitle_time, font_subtitle)
        else:
            x1_subtitle, y1_subtitle, x2_subtitle, y2_subtitle = font_subtitle.getbbox(subtitle_time)
            subtitle_text_width = abs(x2_subtitle - x1_subtitle)
        x_subtitle = (img_template.width - subtitle_text_width) / 2
        text_border(draw, x_subtitle, title_text_height, subtitle_time, font_subtitle, (0, 0, 0), font_color,
                    location1)  # 绘制文字
        # **********************添加卫星和仪器************************
        # 设置卫星、仪器字体
        font_sat = ImageFont.truetype(f'{font_path}', size=legend_sat_loc_size[4])
        # 添加卫星、仪器
        text_border(draw, legend_sat_loc_size[0], legend_sat_loc_size[1], satellite_sensor, font_sat, (0, 0, 0),
                    font_color, location1)  # 绘制文字
        # 添加分辨率
        text_border(draw, legend_sat_loc_size[2], legend_sat_loc_size[3], res, font_sat, (0, 0, 0), font_color,
                    location1)  # 绘制文字
        # **********************添加颜色条************************
        # 添加颜色条
        if len(color_bar_loc_filename) > 0:
            s1 = color_bar_loc_filename[2].replace("LST", prod_name)
            print_with_style(f'颜色条为：{s1}', color='blue')
            img_colorbar = Image.open(s1).convert('RGBA')
            img_template.paste(img_colorbar, (color_bar_loc_filename[0], color_bar_loc_filename[1]),
                               mask=img_colorbar)
    else:
        print_with_style(f"模板尺寸比主图尺寸大，使用外置模板策略", color='cyan')
        img_template.paste(img2, (template_path_size_location[3], template_path_size_location[4]),
                           mask=img2)  # 如果出错去掉mask
        # 创建绘图对象
        draw = ImageDraw.Draw(img_template)
        # 设置标题字体
        font_title = ImageFont.truetype(f'{font_path}', size=title_loc_size[2])
        # 添加标题
        if staid != "FY4A" and staid != "FY4B" and orbits != "X":
            title1 += f"({orbits})"
        if int(pillow_version.split('.')[0]) < 10:  # pillow版本大于10时，使用新版api
            text_width, text_height = draw.textsize(title1, font_title)
        else:
            x1_title, y1_title, x2_title, y2_title = font_title.getbbox(title1)
            text_width = abs(x2_title - x1_title)
            text_height = abs(y2_title - y1_title)
        x_title = (img_template.width - text_width) / 2
        y_title = (template_path_size_location[4] - text_height) / 2
        # 设置副标题字体
        font_subtitle = ImageFont.truetype(f'{font_path}', size=subtitle_loc_size[2])
        # 添加副标题, 增加对月数据和天数据的区别
        subtitle_time = f"{time1[:4]}-{time1[4:6]}-{time1[6:8]} {time1[8:10]}:{time1[10:12]}(UTC)"
        if len(time1) == 8:
            subtitle_time = f"{time1[:4]}-{time1[4:6]}-{time1[6:8]}  "
        if "POAM" in os.path.basename(file_path):  # 月数据(旬数据) 2023-06-01~2023-06-30
            subtitle_time = f"{time1[:4]}-{time1[4:6]}-{time1[6:8]}~{time2[:4]}-{time2[4:6]}-{time2[6:8]}"
        elif "POAD" in os.path.basename(file_path):  # 日数据
            subtitle_time = f"{time1[:4]}-{time1[4:6]}-{time1[6:8]}  "
        if int(pillow_version.split('.')[0]) < 10:  # pillow版本大于10时，使用新版api
            subtitle_width, subtitle_height = draw.textsize(subtitle_time, font_subtitle)
        else:
            x1_subtitle, y1_subtitle, x2_subtitle, y2_subtitle = font_subtitle.getbbox(subtitle_time)
            subtitle_width = abs(x2_subtitle - x1_subtitle)
            subtitle_height = abs(y2_subtitle - y1_subtitle)
        sub_y = template_path_size_location[4] - subtitle_height - template_path_size_location[4] / subtitle_height * 2.5
        sub_x = (template_path_size_location[3] + template_path_size_location[1]) - subtitle_width
        if x_title + text_width > sub_x:  # 标题超长的情况
            sub_y += 3
            y_title = int(y_title) + 4
        if len(title_loc_size) > 3:  # 放开标题尺寸限制
            if title_loc_size[3]:
                draw.text((int(title_loc_size[0]), int(title_loc_size[1])), title1, font=font_title,
                          fill=(0, 0, 0))  # 绘制标题
        else:
            draw.text((x_title, int(y_title)), title1, font=font_title, fill=(0, 0, 0))  # 绘制标题
        if len(subtitle_loc_size) > 3:  # 放开副标题尺寸限制
            if subtitle_loc_size[3]:
                draw.text((subtitle_loc_size[0], subtitle_loc_size[1]), subtitle_time, font=font_subtitle,
                          fill=(0, 0, 0))  # 绘制副标题
        else:
            draw.text((sub_x, sub_y), subtitle_time, font=font_subtitle, fill=(0, 0, 0))  # 绘制副标题
        # 设置卫星、仪器字体
        font_sat = ImageFont.truetype(f'{font_path}', size=legend_sat_loc_size[4])
        # 添加卫星、仪器
        draw.text((legend_sat_loc_size[0], legend_sat_loc_size[1]), satellite_sensor, font=font_sat,
                  fill=(51, 51, 51))
        # 添加分辨率
        draw.text((legend_sat_loc_size[2], legend_sat_loc_size[3]), res, font=font_sat, fill=(51, 51, 51))
    # 添加颜色条
    if len(color_bar_loc_filename) > 0:
        s1 = color_bar_loc_filename[2].replace("LST", prod_name)
        print_with_style(f'颜色条为：{s1}', color='blue')
        img_colorbar = Image.open(s1).convert('RGBA')
        img_template.paste(img_colorbar, (color_bar_loc_filename[0], color_bar_loc_filename[1]), mask=img_colorbar)
    # 添加logo
    if not len(logo_loc_filename) < 1:  # logo控制开关
        img_logo = Image.open(f'{os.getcwd()}/{logo_loc_filename[2]}')
        img_template.paste(img_logo, (logo_loc_filename[0], logo_loc_filename[1]), mask=img_logo)
    # 添加国界线图例
    if not len(legend_country_loc_filename) < 1:
        legend_country = Image.open(f'{os.getcwd()}/{legend_country_loc_filename[2]}')
        img_template.paste(legend_country, (legend_country_loc_filename[0], legend_country_loc_filename[1]),
                           mask=legend_country)
    # 添加未定国界/省界图例
    if not len(legend_province_loc_filename) < 1:
        legend_province = Image.open(f'{os.getcwd()}/{legend_province_loc_filename[2]}')
        img_template.paste(legend_province, (legend_province_loc_filename[0], legend_province_loc_filename[1]),
                           mask=legend_province)
    # 添加海洋图例
    if not len(legend_sea_loc_filename) < 1:
        legend_sea = Image.open(f'{os.getcwd()}/{legend_sea_loc_filename[2]}')
        img_template.paste(legend_sea, (legend_sea_loc_filename[0], legend_sea_loc_filename[1]), mask=legend_sea)
    # 添加陆地图例
    if not len(legend_land_loc_filename) < 1:
        legend_land = Image.open(f'{os.getcwd()}/{legend_land_loc_filename[2]}')
        img_template.paste(legend_land, (legend_land_loc_filename[0], legend_land_loc_filename[1]),
                           mask=legend_land)
    # 图像保存
    img_template = img_template.convert("RGB")
    t2 = time.time()
    print_with_style(f'专题图绘制完成，用时为：🚀{round((t2-t1), 3)}s🚀', color='cyan')
    if is_need_small[2]:
        x1 = int(img_template.size[0] * is_need_small[0])
        y1 = int(img_template.size[1] * is_need_small[1])
        img_template_small = img_template.resize((x1, y1))
        return [img_template, img_template_small]
    else:
        return [img_template]
    # **********************************************************************************************************


# 用于文字边框展示，传入draw,坐标x,y，字体，边框颜色和填充颜色
def text_border(draw, x, y, text, font, shadowcolor, fillcolor, location1):
    if location1 == "EastAsia":
        line_width = 2
    else:
        line_width = 1
    draw.text((x - line_width, y), text, font=font, fill=shadowcolor)
    draw.text((x + line_width, y), text, font=font, fill=shadowcolor)
    draw.text((x, y - line_width), text, font=font, fill=shadowcolor)
    draw.text((x, y + line_width), text, font=font, fill=shadowcolor)
    draw.text((x - line_width, y - line_width), text, font=font, fill=shadowcolor)
    draw.text((x + line_width, y - line_width), text, font=font, fill=shadowcolor)
    draw.text((x - line_width, y + line_width), text, font=font, fill=shadowcolor)
    draw.text((x + line_width, y + line_width), text, font=font, fill=shadowcolor)
    draw.text((x, y), text, font=font, fill=fillcolor)


# 用于边界线图像裁剪
def crop_image_by_bbox(img, bbox):
    width, height = img.size
    x_min = int((bbox[0] + 180) / 360 * width)
    x_max = int((bbox[1] + 180) / 360 * width)
    y_min = int((bbox[3] - 90) / -180 * height)
    y_max = int((bbox[2] - 90) / -180 * height)
    img = np.array(img)
    cropped_img = img[y_min:y_max, x_min:x_max, :]
    img = Image.fromarray(cropped_img)
    return img


def transform_image_coordinates(img, box):
    width, height = img.size
    img = np.array(img)
    # -180~180  ==>  0~360
    if 360 in box:
        left_half = img[:, :width//2, :]
        right_half = img[:, width//2:, :]
    elif 330 in box:
        left_half = img[:, :7 * width // 12, :]
        right_half = img[:, 5 * width // 12:, :]
    elif 180 in box:  # 不需要转变位置的情况
        left_half = img[:, width // 2:, :]
        right_half = img[:, :width // 2, :]
    else:
        raise Exception('当前只支持全球经度为【-180~180, 0~360, -30~330】的情况')
    transformed_img = np.concatenate((right_half, left_half), axis=1)  # 拼接矩阵
    img = Image.fromarray(transformed_img)
    return img
