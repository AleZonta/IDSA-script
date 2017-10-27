import json
import logging
import os
import zipfile

import pyproj as pyproj


def compute():
    path = "/Users/alessandrozonta/Documents/Results Exp/folderfix/1/"
    directories = os.listdir(path)

    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    for el in directories:
        logging.debug("laoding {}".format(el))
        fileName = "/POIs.zip"
        pathLocal = path + "/" + el + fileName
        # totalList.append(pathLocal)
        zf = zipfile.ZipFile(pathLocal)
        filename = "/POIs.JSON"
        zipdata = zf.read(filename)
        json_data = zipdata.replace("(", '"').replace(")", '"')
        data = json.loads(json_data)
        target = data["target"]
        pois = data["POIsLocation"]



if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    fourhundred = [u'52.0455681,4.3302045', u'52.0278086,4.3131448', u'52.0418896,4.3224674', u'52.0384898,4.3142349', u'52.0418903,4.3224427', u'52.0434495,4.3270506', u'52.0292566,4.3118568', u'52.0333342,4.3203774', u'52.0331324,4.3204883', u'52.0333986,4.3203133', u'52.0331056,4.3205031', u'52.0292312,4.3119019', u'52.0498364,4.3342542', u'52.0278985,4.3134658', u'52.0473754,4.3165385', u'52.0333191,4.3203999', u'52.0484813,4.3300169', u'52.0331556,4.3208858', u'52.04347,4.3270887', u'52.0382396,4.3171562', u'52.0262727,4.3102286', u'52.0512112,4.3303774', u'52.040018,4.3187001', u'52.0382683,4.3172588', u'52.0278697,4.3133167', u'52.0285653,4.3145185', u'52.043463,4.3270757', u'52.0361333,4.306447', u'52.0278651,4.3133063', u'52.0377673,4.3166255', u'52.0256047,4.3108319', u'52.0420082,4.3222497', u'52.0488353,4.3206954', u'52.0514956,4.3301465', u'52.0357861,4.3085151', u'52.0342205,4.3097766', u'52.05121,4.3303868', u'52.0431739,4.3265098', u'52.0359923,4.3170381', u'52.0432587,4.32663', u'52.038041,4.315593', u'52.0333737,4.320343', u'52.049835,4.3342543', u'52.0262839,4.3102247', u'52.0418898,4.322469', u'52.0378904,4.3081669', u'52.0406885,4.3185262', u'52.029595,4.3186596', u'52.024838,4.3199658', u'52.0420207,4.3222683', u'52.033385,4.3203381', u'52.0361448,4.3065088', u'52.0480722,4.3344082', u'52.0419832,4.3186147', u'52.049853,4.3342513', u'52.0511985,4.3303898', u'52.0295854,4.3186624', u'52.0412145,4.3221407', u'52.0295935,4.318666', u'52.0248287,4.3199434', u'52.043815,4.3277004', u'52.0492987,4.3321189', u'52.0317443,4.3247461', u'52.0419997,4.3222462', u'52.0400126,4.3186888', u'52.0408044,4.3181877', u'52.0483803,4.329892', u'52.0376272,4.3059953', u'52.0361411,4.3065057', u'52.0279036,4.3134618', u'52.0262819,4.3102231', u'52.0434654,4.3270803', u'52.0492974,4.3321185', u'52.0381751,4.3076232', u'52.039958,4.3192556', u'52.025605,4.3108329', u'52.0498383,4.3342538', u'52.0262919,4.310237', u'52.0317443,4.3247461', u'52.0436691,4.3103056', u'52.0419985,4.3222591', u'52.0430178,4.3279869', u'52.036081,4.3069502', u'52.043299,4.3266882', u'52.0332302,4.3211405', u'52.0388451,4.3209893', u'52.0380055,4.3155999', u'52.0438094,4.3277294', u'52.0353382,4.3065964', u'52.0489654,4.3186877', u'52.029211,4.3118821', u'52.0498418,4.3342531', u'52.0514997,4.3301449', u'52.0399613,4.3192421', u'52.0292105,4.3119214', u'52.0361392,4.3065046', u'52.0248358,4.319963', u'52.0378669,4.3082156', u'52.0409018,4.3123181', u'52.0295915,4.3186641', u'52.0292227,4.3119103', u'52.0278175,4.3131436', u'52.0519609,4.3289971', u'52.0455819,4.3302249', u'52.0498442,4.3342528', u'52.0492949,4.3321179', u'52.0382396,4.3171562', u'52.033391,4.3203399', u'52.0432549,4.3266197', u'52.0465947,4.3350554', u'52.0333887,4.3203477', u'52.0482471,4.3321414', u'52.033287,4.3069197', u'52.0379816,4.3164074', u'52.0404454,4.318815', u'52.0408193,4.3182857', u'52.0378586,4.3082276', u'52.0278748,4.313334', u'52.0498427,4.334253', u'52.0465139,4.3373034', u'52.0357948,4.3084802', u'52.0482943,4.3320499', u'52.0399608,4.3192692', u'52.0292317,4.3119082', u'52.0357728,4.3172116', u'52.0498427,4.334253', u'52.0361362,4.306449', u'52.0295966,4.3186542', u'52.025611,4.3108508', u'52.0278908,4.313476', u'52.0361319,4.3064687', u'52.0380235,4.3163614', u'52.0333342,4.3203774', u'52.0418652,4.3224509', u'52.0455744,4.3302139', u'52.0349666,4.3070022', u'52.0408875,4.312262', u'52.0361539,4.3065106', u'52.0434659,4.327081', u'52.0420175,4.3222759', u'52.0387113,4.3151461', u'52.034969,4.3069949', u'52.0453774,4.3299276', u'52.024538,4.3134543', u'52.0443876,4.3378104', u'52.047968,4.3347007', u'52.0445909,4.3287841', u'52.0429802,4.3280517', u'52.0434684,4.3270856', u'52.0436652,4.3103136', u'52.0439029,4.3260947', u'52.0455171,4.3287207', u'52.0486675,4.3325366', u'52.0295957,4.3186619', u'52.0278762,4.3133412', u'52.0361674,4.3065725', u'52.0387093,4.3151462', u'52.0512241,4.3303888', u'52.0434631,4.3270758', u'52.0420137,4.3222765', u'52.0515143,4.3301516', u'52.0453756,4.3299251', u'52.0358065,4.3084976', u'52.0488677,4.3208012', u'52.0492943,4.3321179', u'52.0349964,4.3226029', u'52.0420113,4.3222656', u'52.0278936,4.3134946', u'52.0377293,4.3239384', u'52.0455743,4.3302138', u'52.0377994,4.31659', u'52.025602,4.310825', u'52.0482943,4.3320499', u'52.0278955,4.3134788', u'52.0292175,4.3119151', u'52.0519694,4.329071', u'52.0256082,4.3108421', u'52.0357805,4.3172326', u'52.041868,4.3224645', u'52.0482827,4.3320487', u'52.0256027,4.310826', u'52.0481155,4.3323535', u'52.0432547,4.3093594', u'52.0487563,4.3334502', u'52.0295937,4.3186619', u'52.040888,4.3122705', u'52.0380371,4.3155915', u'52.0292155,4.3119172', u'52.0292289,4.3119214', u'52.0505299,4.3304314', u'52.0256056,4.3108344', u'52.0333262,4.3203737', u'52.0344699,4.3096396', u'52.0431792,4.326562', u'52.0482736,4.3320995', u'52.0333072,4.320352', u'52.0378616,4.3079963', u'52.0262717,4.3102372', u'52.0333612,4.3203679', u'52.0296258,4.3097963', u'52.0256167,4.3108675', u'52.0432916,4.3266871', u'52.0333629,4.3203598', u'52.0292063,4.3119178', u'52.0482985,4.3320455', u'52.0359907,4.317015', u'52.0380168,4.3155995', u'52.0455831,4.3302196', u'52.0349594,4.3070151', u'52.0380278,4.3155894', u'52.0406948,4.31853', u'52.0292361,4.3118965', u'52.0387106,4.3151743', u'52.0248398,4.3199704', u'52.0436939,4.3104358', u'52.0418962,4.3224407', u'52.0483803,4.329892', u'52.0402753,4.321565', u'52.0408875,4.312262', u'52.0262799,4.3102259', u'52.0382577,4.3172138', u'52.0380477,4.3155682', u'52.0248251,4.3199421', u'52.0295921,4.3186661', u'52.0498452,4.3342527', u'52.0384916,4.314245', u'52.037734,4.3167027', u'52.0316151,4.324893', u'52.0342211,4.3097641', u'52.0378204,4.3080399', u'52.0349625,4.3070152', u'52.0380235,4.3163614', u'52.0262702,4.3102312', u'52.0452778,4.3373816', u'52.0380569,4.3155647', u'52.0292399,4.3119053', u'52.0418652,4.3224509', u'52.0498448,4.3342527', u'52.0519609,4.3289971', u'52.048044,4.3251187', u'52.0332442,4.3211213', u'52.0379816,4.3164074', u'52.0383947,4.3172058', u'52.045576,4.3302163', u'52.0332275,4.3211295', u'52.0292334,4.3119038', u'52.0498479,4.3342522', u'52.0505535,4.330485', u'52.0482347,4.3321698', u'52.0472872,4.3359579', u'52.0407569,4.3121973', u'52.0407664,4.3122111', u'52.0515221,4.3301566', u'52.0505542,4.3304949', u'52.04985,4.3342519', u'52.0381702,4.3076226', u'52.036142,4.3065037', u'52.0292148,4.311908', u'52.0278113,4.313144', u'52.0333262,4.3203737', u'52.0452889,4.328436', u'52.0333371,4.3203819', u'52.0409018,4.3123181', u'52.0333108,4.3203695', u'52.0498353,4.3342543', u'52.0387106,4.3151743', u'52.0400647,4.3206019', u'52.0472894,4.3257981', u'52.0453124,4.3374993', u'52.0278508,4.313267', u'52.0332255,4.3209877', u'52.0332349,4.3211219', u'52.0498479,4.3342522', u'52.0498993,4.3219274', u'52.0498493,4.3342519', u'52.0436571,4.31033', u'52.0455999,4.3384066', u'52.0434654,4.3270803', u'52.0511986,4.3303837', u'52.0434684,4.3270856', u'52.0361384,4.3065033', u'52.0376063,4.3059799', u'52.0429952,4.3085131', u'52.0419979,4.3222185', u'52.0419631,4.3185746', u'52.0493001,4.3321192', u'52.0380695,4.3163772', u'52.0465947,4.3350554', u'52.0285653,4.3145185', u'52.0439475,4.3260826', u'52.0443975,4.337812', u'52.0412497,4.3220891', u'52.0491646,4.3319235', u'52.0361525,4.3065092', u'52.0292151,4.3119039', u'52.0380162,4.3156007', u'52.0361311,4.3064551', u'52.0512083,4.3303733', u'52.0419992,4.322265', u'52.0378647,4.3082046', u'52.0383875,4.3171601', u'52.0332306,4.3211185', u'52.0498479,4.3342522', u'52.0498457,4.3342525', u'52.0402847,4.3215678', u'52.0499296,4.3218987', u'52.0399625,4.3192666', u'52.0459828,4.3027996', u'52.0465103,4.3372969', u'52.0487563,4.3334502', u'52.0361367,4.3064805', u'52.0516528,4.3306915', u'52.036144,4.3065066', u'52.0434631,4.3270758', u'52.0516057,4.3305446', u'52.0378481,4.308005', u'52.0330812,4.3206556', u'52.0377832,4.3166026', u'52.0382258,4.3171491', u'52.0292204,4.3119185', u'52.0333772,4.3203426', u'52.0418785,4.3224627', u'52.0332293,4.3211304', u'52.0376295,4.3211196', u'52.0494939,4.3218743', u'52.043183,4.3265165', u'52.04983,4.3342551', u'52.0420177,4.3222596', u'52.0384075,4.3172311', u'52.0378446,4.3080065', u'52.0382565,4.3172537', u'52.0262735,4.3102324', u'52.0418893,4.3224652', u'52.0491713,4.3319094', u'52.0292706,4.3098899', u'52.0515002,4.3301452', u'52.0465124,4.3372423', u'52.0512077,4.3303881', u'52.0348362,4.3098003', u'52.0431852,4.3264852', u'52.0483896,4.3298826', u'52.026274,4.3102324', u'52.048164,4.3322799', u'52.0387093,4.3151462', u'52.04984,4.3342535', u'52.0498925,4.3218956', u'52.0432788,4.3266794', u'52.0278917,4.3134778', u'52.0347919,4.3097352', u'52.0466088,4.3350852', u'52.047273,4.3359116', u'52.033153,4.3208847', u'52.0332178,4.3209929', u'52.0487295,4.3312072', u'52.0380411,4.3155839', u'52.0361546,4.3065443', u'52.0255943,4.3108144', u'52.0511969,4.3303822', u'52.0278985,4.3134658', u'52.0498491,4.3342521', u'52.0333936,4.3203231', u'52.0453761,4.3299257', u'52.051666,4.3307314', u'52.0408891,4.3122437', u'52.0455704,4.3302081', u'52.0498392,4.3342537', u'52.04985,4.3342519', u'52.0256041,4.31083', u'52.049296,4.3321182', u'52.0292346,4.3118799', u'52.0419832,4.3186147', u'52.0498457,4.3342525', u'52.0378022,4.3165826', u'52.0245339,4.3132892', u'52.0473766,4.3165449', u'52.0378022,4.3165826', u'52.0498554,4.3342509', u'52.04984,4.3342535', u'52.0361464,4.3064389', u'52.0451864,4.3296343', u'52.0279005,4.3134715', u'52.0456114,4.3289093', u'52.0516609,4.3307128', u'52.0439029,4.3260947', u'52.04983,4.3342551', u'52.037791,4.3213158', u'52.0498373,4.3342539', u'52.0404198,4.3214376', u'52.0292097,4.311901', u'52.046493,4.3372973', u'52.0453012,4.3284441', u'52.0361259,4.3064613', u'52.0247651,4.3160586', u'52.0405764,4.3179367', u'52.0487603,4.3312897', u'52.0505385,4.3304369', u'52.0412497,4.3220891', u'52.0498422,4.3342532', u'52.0498392,4.3342537', u'52.0419926,4.3222454']
    threhundred = [u'52.0455681,4.3302045', u'52.0278086,4.3131448', u'52.0418896,4.3224674', u'52.0384898,4.3142349', u'52.0418903,4.3224427', u'52.0434495,4.3270506', u'52.0292566,4.3118568', u'52.0333342,4.3203774', u'52.0331324,4.3204883', u'52.0333986,4.3203133', u'52.0331056,4.3205031', u'52.0292312,4.3119019', u'52.0498364,4.3342542', u'52.0278985,4.3134658', u'52.0473754,4.3165385', u'52.0333191,4.3203999', u'52.0484813,4.3300169', u'52.0331556,4.3208858', u'52.04347,4.3270887', u'52.0382396,4.3171562', u'52.0262727,4.3102286', u'52.0512112,4.3303774', u'52.040018,4.3187001', u'52.0382683,4.3172588', u'52.0278697,4.3133167', u'52.0285653,4.3145185', u'52.043463,4.3270757', u'52.0361333,4.306447', u'52.0278651,4.3133063', u'52.0377673,4.3166255', u'52.0256047,4.3108319', u'52.0420082,4.3222497', u'52.0488353,4.3206954', u'52.0514956,4.3301465', u'52.0357861,4.3085151', u'52.0342205,4.3097766', u'52.05121,4.3303868', u'52.0431739,4.3265098', u'52.0359923,4.3170381', u'52.0432587,4.32663', u'52.038041,4.315593', u'52.0333737,4.320343', u'52.049835,4.3342543', u'52.0262839,4.3102247', u'52.0418898,4.322469', u'52.0378904,4.3081669', u'52.0406885,4.3185262', u'52.029595,4.3186596', u'52.024838,4.3199658', u'52.0420207,4.3222683', u'52.033385,4.3203381', u'52.0361448,4.3065088', u'52.0480722,4.3344082', u'52.0419832,4.3186147', u'52.049853,4.3342513', u'52.0511985,4.3303898', u'52.0295854,4.3186624', u'52.0412145,4.3221407', u'52.0295935,4.318666', u'52.0248287,4.3199434', u'52.043815,4.3277004', u'52.0492987,4.3321189', u'52.0317443,4.3247461', u'52.0419997,4.3222462', u'52.0400126,4.3186888', u'52.0408044,4.3181877', u'52.0483803,4.329892', u'52.0376272,4.3059953', u'52.0361411,4.3065057', u'52.0279036,4.3134618', u'52.0262819,4.3102231', u'52.0434654,4.3270803', u'52.0492974,4.3321185', u'52.0381751,4.3076232', u'52.039958,4.3192556', u'52.025605,4.3108329', u'52.0498383,4.3342538', u'52.0262919,4.310237', u'52.0317443,4.3247461', u'52.0436691,4.3103056', u'52.0419985,4.3222591', u'52.0430178,4.3279869', u'52.036081,4.3069502', u'52.043299,4.3266882', u'52.0332302,4.3211405', u'52.0388451,4.3209893', u'52.0380055,4.3155999', u'52.0438094,4.3277294', u'52.0353382,4.3065964', u'52.0489654,4.3186877', u'52.029211,4.3118821', u'52.0498418,4.3342531', u'52.0514997,4.3301449', u'52.0399613,4.3192421', u'52.0292105,4.3119214', u'52.0361392,4.3065046', u'52.0248358,4.319963', u'52.0378669,4.3082156', u'52.0409018,4.3123181', u'52.0295915,4.3186641', u'52.0292227,4.3119103', u'52.0278175,4.3131436', u'52.0519609,4.3289971', u'52.0455819,4.3302249', u'52.0498442,4.3342528', u'52.0492949,4.3321179', u'52.0382396,4.3171562', u'52.033391,4.3203399', u'52.0432549,4.3266197', u'52.0465947,4.3350554', u'52.0333887,4.3203477', u'52.0482471,4.3321414', u'52.033287,4.3069197', u'52.0379816,4.3164074', u'52.0404454,4.318815', u'52.0408193,4.3182857', u'52.0378586,4.3082276', u'52.0278748,4.313334', u'52.0498427,4.334253', u'52.0465139,4.3373034', u'52.0357948,4.3084802', u'52.0482943,4.3320499', u'52.0399608,4.3192692', u'52.0292317,4.3119082', u'52.0357728,4.3172116', u'52.0498427,4.334253', u'52.0361362,4.306449', u'52.0295966,4.3186542', u'52.025611,4.3108508', u'52.0278908,4.313476', u'52.0361319,4.3064687', u'52.0380235,4.3163614', u'52.0333342,4.3203774', u'52.0418652,4.3224509', u'52.0455744,4.3302139', u'52.0349666,4.3070022', u'52.0408875,4.312262', u'52.0361539,4.3065106', u'52.0434659,4.327081', u'52.0420175,4.3222759', u'52.0387113,4.3151461', u'52.034969,4.3069949', u'52.0453774,4.3299276', u'52.024538,4.3134543', u'52.0443876,4.3378104', u'52.047968,4.3347007', u'52.0445909,4.3287841', u'52.0429802,4.3280517', u'52.0434684,4.3270856', u'52.0436652,4.3103136', u'52.0439029,4.3260947', u'52.0455171,4.3287207', u'52.0486675,4.3325366', u'52.0295957,4.3186619', u'52.0278762,4.3133412', u'52.0361674,4.3065725', u'52.0387093,4.3151462', u'52.0512241,4.3303888', u'52.0434631,4.3270758', u'52.0420137,4.3222765', u'52.0515143,4.3301516', u'52.0453756,4.3299251', u'52.0358065,4.3084976', u'52.0488677,4.3208012', u'52.0492943,4.3321179', u'52.0349964,4.3226029', u'52.0420113,4.3222656', u'52.0278936,4.3134946', u'52.0377293,4.3239384', u'52.0455743,4.3302138', u'52.0377994,4.31659', u'52.025602,4.310825', u'52.0482943,4.3320499', u'52.0278955,4.3134788', u'52.0292175,4.3119151', u'52.0519694,4.329071', u'52.0256082,4.3108421', u'52.0357805,4.3172326', u'52.041868,4.3224645', u'52.0482827,4.3320487', u'52.0256027,4.310826', u'52.0481155,4.3323535', u'52.0432547,4.3093594', u'52.0487563,4.3334502', u'52.0295937,4.3186619', u'52.040888,4.3122705', u'52.0380371,4.3155915', u'52.0292155,4.3119172', u'52.0292289,4.3119214', u'52.0505299,4.3304314', u'52.0256056,4.3108344', u'52.0333262,4.3203737', u'52.0344699,4.3096396', u'52.0431792,4.326562', u'52.0482736,4.3320995', u'52.0333072,4.320352', u'52.0378616,4.3079963', u'52.0262717,4.3102372', u'52.0333612,4.3203679', u'52.0296258,4.3097963', u'52.0256167,4.3108675', u'52.0432916,4.3266871', u'52.0333629,4.3203598', u'52.0292063,4.3119178', u'52.0482985,4.3320455', u'52.0359907,4.317015', u'52.0380168,4.3155995', u'52.0455831,4.3302196', u'52.0349594,4.3070151', u'52.0380278,4.3155894', u'52.0406948,4.31853', u'52.0292361,4.3118965', u'52.0387106,4.3151743', u'52.0248398,4.3199704', u'52.0436939,4.3104358', u'52.0418962,4.3224407', u'52.0483803,4.329892', u'52.0402753,4.321565', u'52.0408875,4.312262', u'52.0262799,4.3102259', u'52.0382577,4.3172138', u'52.0380477,4.3155682', u'52.0248251,4.3199421', u'52.0295921,4.3186661', u'52.0498452,4.3342527', u'52.0384916,4.314245', u'52.037734,4.3167027', u'52.0316151,4.324893', u'52.0342211,4.3097641', u'52.0378204,4.3080399', u'52.0349625,4.3070152', u'52.0380235,4.3163614', u'52.0262702,4.3102312', u'52.0452778,4.3373816', u'52.0380569,4.3155647', u'52.0292399,4.3119053', u'52.0418652,4.3224509', u'52.0498448,4.3342527', u'52.0519609,4.3289971', u'52.048044,4.3251187', u'52.0332442,4.3211213', u'52.0379816,4.3164074', u'52.0383947,4.3172058', u'52.045576,4.3302163', u'52.0332275,4.3211295', u'52.0292334,4.3119038', u'52.0498479,4.3342522', u'52.0505535,4.330485', u'52.0482347,4.3321698', u'52.0472872,4.3359579', u'52.0407569,4.3121973', u'52.0407664,4.3122111', u'52.0515221,4.3301566', u'52.0505542,4.3304949', u'52.04985,4.3342519', u'52.0381702,4.3076226', u'52.036142,4.3065037', u'52.0292148,4.311908', u'52.0278113,4.313144', u'52.0333262,4.3203737', u'52.0452889,4.328436', u'52.0333371,4.3203819', u'52.0409018,4.3123181', u'52.0333108,4.3203695', u'52.0498353,4.3342543', u'52.0387106,4.3151743', u'52.0400647,4.3206019', u'52.0472894,4.3257981', u'52.0453124,4.3374993', u'52.0278508,4.313267', u'52.0332255,4.3209877', u'52.0332349,4.3211219', u'52.0498479,4.3342522', u'52.0498993,4.3219274', u'52.0498493,4.3342519', u'52.0436571,4.31033', u'52.0455999,4.3384066', u'52.0434654,4.3270803', u'52.0511986,4.3303837', u'52.0434684,4.3270856', u'52.0361384,4.3065033', u'52.0376063,4.3059799', u'52.0429952,4.3085131', u'52.0419979,4.3222185', u'52.0419631,4.3185746', u'52.0493001,4.3321192', u'52.0380695,4.3163772', u'52.0465947,4.3350554', u'52.0285653,4.3145185', u'52.0439475,4.3260826', u'52.0443975,4.337812', u'52.0412497,4.3220891', u'52.0491646,4.3319235', u'52.0361525,4.3065092', u'52.0292151,4.3119039', u'52.0380162,4.3156007', u'52.0361311,4.3064551', u'52.0512083,4.3303733', u'52.0419992,4.322265', u'52.0378647,4.3082046']
    twohundred = [u'52.0455681,4.3302045', u'52.0278086,4.3131448', u'52.0418896,4.3224674', u'52.0384898,4.3142349', u'52.0418903,4.3224427', u'52.0434495,4.3270506', u'52.0292566,4.3118568', u'52.0333342,4.3203774', u'52.0331324,4.3204883', u'52.0333986,4.3203133', u'52.0331056,4.3205031', u'52.0292312,4.3119019', u'52.0498364,4.3342542', u'52.0278985,4.3134658', u'52.0473754,4.3165385', u'52.0333191,4.3203999', u'52.0484813,4.3300169', u'52.0331556,4.3208858', u'52.04347,4.3270887', u'52.0382396,4.3171562', u'52.0262727,4.3102286', u'52.0512112,4.3303774', u'52.040018,4.3187001', u'52.0382683,4.3172588', u'52.0278697,4.3133167', u'52.0285653,4.3145185', u'52.043463,4.3270757', u'52.0361333,4.306447', u'52.0278651,4.3133063', u'52.0377673,4.3166255', u'52.0256047,4.3108319', u'52.0420082,4.3222497', u'52.0488353,4.3206954', u'52.0514956,4.3301465', u'52.0357861,4.3085151', u'52.0342205,4.3097766', u'52.05121,4.3303868', u'52.0431739,4.3265098', u'52.0359923,4.3170381', u'52.0432587,4.32663', u'52.038041,4.315593', u'52.0333737,4.320343', u'52.049835,4.3342543', u'52.0262839,4.3102247', u'52.0418898,4.322469', u'52.0378904,4.3081669', u'52.0406885,4.3185262', u'52.029595,4.3186596', u'52.024838,4.3199658', u'52.0420207,4.3222683', u'52.033385,4.3203381', u'52.0361448,4.3065088', u'52.0480722,4.3344082', u'52.0419832,4.3186147', u'52.049853,4.3342513', u'52.0511985,4.3303898', u'52.0295854,4.3186624', u'52.0412145,4.3221407', u'52.0295935,4.318666', u'52.0248287,4.3199434', u'52.043815,4.3277004', u'52.0492987,4.3321189', u'52.0317443,4.3247461', u'52.0419997,4.3222462', u'52.0400126,4.3186888', u'52.0408044,4.3181877', u'52.0483803,4.329892', u'52.0376272,4.3059953', u'52.0361411,4.3065057', u'52.0279036,4.3134618', u'52.0262819,4.3102231', u'52.0434654,4.3270803', u'52.0492974,4.3321185', u'52.0381751,4.3076232', u'52.039958,4.3192556', u'52.025605,4.3108329', u'52.0498383,4.3342538', u'52.0262919,4.310237', u'52.0317443,4.3247461', u'52.0436691,4.3103056', u'52.0419985,4.3222591', u'52.0430178,4.3279869', u'52.036081,4.3069502', u'52.043299,4.3266882', u'52.0332302,4.3211405', u'52.0388451,4.3209893', u'52.0380055,4.3155999', u'52.0438094,4.3277294', u'52.0353382,4.3065964', u'52.0489654,4.3186877', u'52.029211,4.3118821', u'52.0498418,4.3342531', u'52.0514997,4.3301449', u'52.0399613,4.3192421', u'52.0292105,4.3119214', u'52.0361392,4.3065046', u'52.0248358,4.319963', u'52.0378669,4.3082156', u'52.0409018,4.3123181', u'52.0295915,4.3186641', u'52.0292227,4.3119103', u'52.0278175,4.3131436', u'52.0519609,4.3289971', u'52.0455819,4.3302249', u'52.0498442,4.3342528', u'52.0492949,4.3321179', u'52.0382396,4.3171562', u'52.033391,4.3203399', u'52.0432549,4.3266197', u'52.0465947,4.3350554', u'52.0333887,4.3203477', u'52.0482471,4.3321414', u'52.033287,4.3069197', u'52.0379816,4.3164074', u'52.0404454,4.318815', u'52.0408193,4.3182857', u'52.0378586,4.3082276', u'52.0278748,4.313334', u'52.0498427,4.334253', u'52.0465139,4.3373034', u'52.0357948,4.3084802', u'52.0482943,4.3320499', u'52.0399608,4.3192692', u'52.0292317,4.3119082', u'52.0357728,4.3172116', u'52.0498427,4.334253', u'52.0361362,4.306449', u'52.0295966,4.3186542', u'52.025611,4.3108508', u'52.0278908,4.313476', u'52.0361319,4.3064687', u'52.0380235,4.3163614', u'52.0333342,4.3203774', u'52.0418652,4.3224509', u'52.0455744,4.3302139', u'52.0349666,4.3070022', u'52.0408875,4.312262', u'52.0361539,4.3065106', u'52.0434659,4.327081', u'52.0420175,4.3222759', u'52.0387113,4.3151461', u'52.034969,4.3069949', u'52.0453774,4.3299276', u'52.024538,4.3134543', u'52.0443876,4.3378104', u'52.047968,4.3347007', u'52.0445909,4.3287841', u'52.0429802,4.3280517', u'52.0434684,4.3270856', u'52.0436652,4.3103136', u'52.0439029,4.3260947', u'52.0455171,4.3287207', u'52.0486675,4.3325366', u'52.0295957,4.3186619', u'52.0278762,4.3133412', u'52.0361674,4.3065725', u'52.0387093,4.3151462', u'52.0512241,4.3303888', u'52.0434631,4.3270758', u'52.0420137,4.3222765', u'52.0515143,4.3301516', u'52.0453756,4.3299251', u'52.0358065,4.3084976', u'52.0488677,4.3208012', u'52.0492943,4.3321179', u'52.0349964,4.3226029', u'52.0420113,4.3222656', u'52.0278936,4.3134946', u'52.0377293,4.3239384', u'52.0455743,4.3302138', u'52.0377994,4.31659', u'52.025602,4.310825', u'52.0482943,4.3320499', u'52.0278955,4.3134788', u'52.0292175,4.3119151', u'52.0519694,4.329071', u'52.0256082,4.3108421', u'52.0357805,4.3172326', u'52.041868,4.3224645', u'52.0482827,4.3320487', u'52.0256027,4.310826', u'52.0481155,4.3323535', u'52.0432547,4.3093594', u'52.0487563,4.3334502', u'52.0295937,4.3186619', u'52.040888,4.3122705', u'52.0380371,4.3155915', u'52.0292155,4.3119172', u'52.0292289,4.3119214', u'52.0505299,4.3304314', u'52.0256056,4.3108344', u'52.0333262,4.3203737', u'52.0344699,4.3096396', u'52.0431792,4.326562', u'52.0482736,4.3320995', u'52.0333072,4.320352', u'52.0378616,4.3079963', u'52.0262717,4.3102372', u'52.0333612,4.3203679', u'52.0296258,4.3097963']
    onehundred = [u'52.0455681,4.3302045', u'52.0278086,4.3131448', u'52.0418896,4.3224674', u'52.0384898,4.3142349', u'52.0418903,4.3224427', u'52.0434495,4.3270506', u'52.0292566,4.3118568', u'52.0333342,4.3203774', u'52.0331324,4.3204883', u'52.0333986,4.3203133', u'52.0331056,4.3205031', u'52.0292312,4.3119019', u'52.0498364,4.3342542', u'52.0278985,4.3134658', u'52.0473754,4.3165385', u'52.0333191,4.3203999', u'52.0484813,4.3300169', u'52.0331556,4.3208858', u'52.04347,4.3270887', u'52.0382396,4.3171562', u'52.0262727,4.3102286', u'52.0512112,4.3303774', u'52.040018,4.3187001', u'52.0382683,4.3172588', u'52.0278697,4.3133167', u'52.0285653,4.3145185', u'52.043463,4.3270757', u'52.0361333,4.306447', u'52.0278651,4.3133063', u'52.0377673,4.3166255', u'52.0256047,4.3108319', u'52.0420082,4.3222497', u'52.0488353,4.3206954', u'52.0514956,4.3301465', u'52.0357861,4.3085151', u'52.0342205,4.3097766', u'52.05121,4.3303868', u'52.0431739,4.3265098', u'52.0359923,4.3170381', u'52.0432587,4.32663', u'52.038041,4.315593', u'52.0333737,4.320343', u'52.049835,4.3342543', u'52.0262839,4.3102247', u'52.0418898,4.322469', u'52.0378904,4.3081669', u'52.0406885,4.3185262', u'52.029595,4.3186596', u'52.024838,4.3199658', u'52.0420207,4.3222683', u'52.033385,4.3203381', u'52.0361448,4.3065088', u'52.0480722,4.3344082', u'52.0419832,4.3186147', u'52.049853,4.3342513', u'52.0511985,4.3303898', u'52.0295854,4.3186624', u'52.0412145,4.3221407', u'52.0295935,4.318666', u'52.0248287,4.3199434', u'52.043815,4.3277004', u'52.0492987,4.3321189', u'52.0317443,4.3247461', u'52.0419997,4.3222462', u'52.0400126,4.3186888', u'52.0408044,4.3181877', u'52.0483803,4.329892', u'52.0376272,4.3059953', u'52.0361411,4.3065057', u'52.0279036,4.3134618', u'52.0262819,4.3102231', u'52.0434654,4.3270803', u'52.0492974,4.3321185', u'52.0381751,4.3076232', u'52.039958,4.3192556', u'52.025605,4.3108329', u'52.0498383,4.3342538', u'52.0262919,4.310237', u'52.0317443,4.3247461', u'52.0436691,4.3103056', u'52.0419985,4.3222591', u'52.0430178,4.3279869', u'52.036081,4.3069502', u'52.043299,4.3266882', u'52.0332302,4.3211405', u'52.0388451,4.3209893', u'52.0380055,4.3155999', u'52.0438094,4.3277294', u'52.0353382,4.3065964', u'52.0489654,4.3186877', u'52.029211,4.3118821', u'52.0498418,4.3342531', u'52.0514997,4.3301449', u'52.0399613,4.3192421', u'52.0292105,4.3119214', u'52.0361392,4.3065046', u'52.0248358,4.319963', u'52.0378669,4.3082156', u'52.0409018,4.3123181', u'52.0295915,4.3186641']

    test = 0

    logging.debug("End Program")