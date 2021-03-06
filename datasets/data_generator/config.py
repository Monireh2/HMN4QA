# -*- coding: utf8 -*-
"""
    The configure of the data generator for HMN4QA
    COLING2016 - Hierarchical Memory Networks for Answer Selection on Unknown Words
"""

familyName_ch = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楮', '卫', '蒋', '沈', '韩', '杨', '朱',
                 '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢',
                 '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌',
                 '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛',
                 '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮',
                 '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵',
                 '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                 '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闽', '席', '季', '麻', '强',
                 '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆', '高',
                 '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房',
                 '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左',
                 '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠',
                 '甄', '麹', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌',
                 '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲',
                 '伊', '宫', '欧阳', '太史', '端木', '上官', '司马', '东方', '独孤', '南宫', '万俟', '闻人', '夏侯',
                 '诸葛', '尉迟', '公羊']

firstName_female_ch = ['秀英', '桂英', '英', '秀兰', '萍', '玉梅', '红', '丽', '敏', '芳', '静', '红梅', '霞', '燕',
                       '娟', '娜', '丹', '玲', '婷婷', '雪', '倩', '颖', '婷', '悦', '洁', '妍', '玥', '涵', '馨', '蕊',
                       '雨萌', '梓琳', '欣', '子琳', '思思', '雨萱', '自怡', '若彤', '思琪', '佳', '可', '琨瑜' ,'兰',
                       '兰蕙', '梦', '兰泽', '岚翠', '欣怡', '梓涵', '晨曦', '紫涵', '诗涵', '梦琪', '嘉怡', '子萱',
                       '雨涵', '可馨', '梓萱', '思涵', '思彤', '心怡', '可欣', '郁馨', '雨馨', '雨欣', '雨彤']

firstName_male_ch = ['军', '勇', '伟', '建国', '建华', '建军', '平', '建平', '斌', '强', '涛', '刚', '波', '辉', '磊',
                     '超', '鹏', '杰', '亮', '浩', '鑫', '帅', '俊杰', '宇', '睿', '博', '瑞', '昊', '子轩', '鑫宇',
                     '梓豪', '和昶', '浩杰', '宇轩', '俊泽', '景曜', '靖', '君浩', '俊艾', '俊拔', '俊弼', '才', '平',
                     '和洽', '和惬', '和硕', '和颂', '风', '蓝', '浩宇', '浩然', '博文', '子涵', '雨泽', '皓轩', '梓轩',
                     '文博', '峻熙', '明轩', '致远', '安邦', '安福', '安歌', '安国', '刚捷']

familyName_en = ['Smythe', 'Jones', 'Williams', 'Wright', 'Cartwright', 'Wainwright', 'Smith', 'Wood', 'Field', 'Ford',
                 'Street', 'Cliff', 'Tree', 'Lane', 'Bush', 'Brook', 'Pond', 'Lake', 'Forest', 'Short', 'Brown', 'Long',
                 'Longfellow', 'Johnson', 'Robinson', 'Williamson', 'Parker', 'Eberhardt', 'Good', 'Goodwin', 'Jordan',
                 'Nixon', 'Dixon', 'Newton', 'Baker', 'Weber', 'Webster', 'Smith', 'Sandall', 'Plimmer', 'Arnot', 'Wood',
                 'Price', 'Graham', 'Norman', 'Henry', 'Anjou', 'Richard', 'Edward', 'James', 'Charles', 'Ann', 'George',
                 'Elizabeth', 'Wettin']

firstName_female_en = ['Emily', 'Shirley', 'Fiona', 'Gloria', 'Vivian', 'Joyce', 'Wendy', 'Tracy', 'Nancy', 'Lillian',
                       'Rita', 'Amy', 'Catherine', 'Judy', 'Jessica', 'Joy', 'Yolanda', 'Xena', 'Laney', 'Eva', 'Sarah',
                       'May', 'Demi', 'Linda', 'Sylvia', 'Debbie', 'Veronica', 'Leslie', 'Grace', 'Rebecca', 'Cindy',
                       'Ada', 'Angela', 'Michelle', 'Lisa', 'Sherry', 'Carina', 'Sally', 'Melody', 'Jane', 'Ann', 'Mary',
                       'Alice', 'Olivia', 'Sophia', 'Hannah', 'Teresa', 'Annie', 'Sunny', 'Elaine', 'Rachel', 'Cherry',
                       'Cynthia', 'Diana', 'Candice', 'Vicky', 'Xochitl', 'Caroline', 'Kate', 'Christina', 'Crystal',
                       'Laura', 'Belinda', 'Claire', 'Ava', 'Sabrina', 'Bella', 'Winnie', 'Phoebe', 'Ximena', 'Tina',
                       'Zoey', 'Irene', 'Jasmine', 'Cheryl', 'Iris', 'Jocelyn', 'Victoria', 'Stella', 'Nicole', 'Cathy',
                       'Daisy', 'Tiffany', 'Fanny', 'Josie', 'Anne', 'Vanessa', 'Angel', 'Sara', 'Flora',
                       'Amber', 'Joanna', 'Athena', 'Alexis', 'Aimee', 'Agnes', 'Queenie', 'Silvia', 'Serena',
                       'Emma', 'Zoe', 'April', 'Mandy', 'Chloe', 'Jenny', 'Cassie', 'Eileen', 'Gina',
                       'Natalie', 'Lucy', 'Maggie', 'Ally', 'Summer', 'Anna', 'Terry', 'Chelsea', 'Vera',
                       'Mia', 'Faye', 'Jaycee', 'Cecilia', 'Candy', 'Dora', 'Vivi', 'Xanthe', 'Lana']

firstName_male_en = ['Shirley', 'Vincent', 'Eason', 'Kevin', 'Andy', 'Vivian', 'Joyce', 'Tracy', 'Nancy', 'Johnny',
                     'Jessica', 'Joy', 'Allen', 'Amanda', 'Gary', 'David', 'Jeff', 'Abby', 'Lynn', 'Jacky', 'Fred',
                     'Alex', 'Michael', 'Jonny', 'Leo', 'Peter', 'Taylor', 'Kelly', 'Sean', 'Jack', 'Carol', 'Sam',
                     'Albert', 'Eric', 'Alan', 'Caesar', 'Jason', 'Jessie', 'Louis', 'Thomas', 'Shawn', 'Robert',
                     'Jacob', 'Bruce', 'Tony', 'Lucas', 'Aaron', 'Betty', 'Paul', 'Quinn', 'Kris', 'Simon', 'Chris',
                     'Helen', 'Max', 'Gavin', 'Howard', 'Ethan', 'Nicholas', 'Mark', 'Joan', 'Jerry',
                     'Stephen', 'Joost', 'Landi', 'Daniel', 'George', 'Karen', 'Joshua', 'Yvonne', 'Tom',
                     'Sandy', 'John', 'Martin', 'Steven', 'Carlyle', 'Matthew', 'Oliver', 'Bill', 'Jayden',
                     'Victor', 'Connie', 'Francis', 'Bonnie', 'Rain', 'Erin', 'Jimmy', 'Joseph', 'Lawrence',
                     'Joe', 'Lucky', 'Nick', 'Ken', 'Carl', 'Xavier', 'Evan', 'Ian', 'Edison',
                     'Lance', 'Vince', 'Carlton', 'Jeffrey', 'Ryan', 'Jesus', 'Hank', 'Jon', 'Xander',
                     'Ivan', 'Lewis', 'Harvey', 'Roger', 'Benjamin', 'Harry', 'Mike', 'Vin', 'Hans']

locationDict_ch = [
               ['北京', '上海', '天津', '西安', '杭州', '大连', '青岛', '福州', '厦门', '昆明', '南京', '汕头', '桂林',
                '成都', '广州', '海口', '长沙', '烟台', '重庆', '温州', '三亚', '哈尔滨', '深圳', '南昌', '香港',
                '澳门', '台北', '高雄', '东京', '大阪', '名古屋', '札幌', '福冈', '冲绳', '汉城', '釜山', '新加坡',
                '吉隆坡', '槟城', '怡保', '曼谷', '清迈', '普吉岛', '古晋', '雅加达', '巴里岛', '棉兰', '巨港', '泗水',
                '仰光', '河内', '金边', '西贡', '永珍', '马尼拉', '宿雾', '帝力', '阿皮亚', '达喀尔', '诗邬', '塞班',
                '汶来', '新得里', '喀布尔', '吉大港', '卡拉奇', '汤加大埔', '瑙鲁', '碧港', '孟买', '科伦坡',
                '加尔各答', '马德拉斯', '加得满都', '墨西哥', '圣萨尔瓦多', '巴拿马', '哈瓦讷', '波哥大', '基多',
                '利马', '圣地亚哥', '布宜诺艾利斯', '圣保罗', '里约热内卢', '巴西利亚', '加拉加斯', '开雪', '蒙地维多',
                '马拿瓜', '危地马拉', '圣多明各', '拉巴斯', '京士顿', '圣湖安', '太子港', '蒙特哥湾', '圣何塞',
                '德古斯加巴', '亚加普科', '桥镇', '西班牙港', '亚松森', '玛瑙斯', '雷雪夫', '帕拉马里博', '乔治市',
                '伦敦', '巴黎', '日内瓦', '苏黎世', '柏林', '汉堡', '法兰克福', '科隆', '幕尼黑', '都伯林', '汕隆',
                '华沙', '阿姆斯特丹', '布鲁塞尔', '维也纳', '布拉格', '布达佩斯', '雅典', '米兰', '罗马', '巴塞罗那',
                '波恩', '杜塞道夫', '斯图加特', '爱丁堡', '索非亚', '伊斯坦堡', '里斯本', '马德里', '直布罗陀',
                '贝尔格来得', '布加勒斯', '曼彻斯特', '哥本哈根', '奥斯陆', '斯德哥尔摩', '赫尔辛基', '格拉斯哥',
                '尼斯', '纽约', '费城', '波士顿', '华盛顿', '芝加哥', '底特律', '匹兹堡', '克里夫兰', '水牛城',
                'PEK', 'SHA', 'TSN', 'SIA', 'HGH', 'DLC', 'TAO', 'FOC', 'XMN', 'KMG', 'NKG', 'SWA', 'KWL', 'CTU',
                'HAK', 'CSX', 'YNT', 'CKG', 'WNZ', 'SYX', 'HRB', 'SZX', 'KHN', 'HKG', 'MFM', 'TPE', 'KHH',
                'TYO', 'OSA', 'NGO', 'SPK', 'FUK', 'OKA', 'SEL', 'PUS', 'SIN', 'KUL', 'PEN', 'IPH', 'BKK', 'HKT',
                'KCH', 'JKT', 'DPS', 'MES', 'PLM', 'SUB', 'RGN', 'HAN', 'PENH', 'PNH', 'VTE', 'MNL', 'CEB', 'DIL',
                'KINABALU', 'BKI', 'SBW', 'SPN', 'SERI', 'BWN', 'KBL', 'CGP', 'KHI', 'TBU', 'INU', 'BAG', 'BOM',
                'CMB', 'CCU', 'MAA', 'KTM', 'MEX', 'SAL', 'PTY', 'UIO', 'LIM', 'SCL', 'SAN', 'AIRES',
                'BUE', 'SAO', 'RIO', 'CCS', 'CAY', 'MVD', 'MGA', 'GUA', 'DOMINGO', 'SDQ', 'LPB', 'JUAN', 'SJU',
                'PAP', 'MBJ', 'SJO', 'ACA', 'TOWN', 'BGI', 'POS', 'MAO', 'REL', 'PBM', 'TOWN', 'GRG', 'PAR', 'GVA',
                'ZRH', 'BER', 'HAM', 'FRA', 'CGN', 'MUC', 'DUB', 'SNN', 'WAW', 'AMS', 'BRU', 'VIE', 'PRG', 'BUD',
                'ATH', 'MIL', 'ROM', 'BCN', 'BNJ', 'DUS', 'STR', 'EDI', 'SOF', 'IST', 'LIS', 'MAD', 'GIB', 'BEG',
                'BUH', 'MAN', 'CPH', 'OSL', 'STO', 'HEL', 'GLA', 'NCE', 'NYK', 'PHL', 'BOS', 'CHI', 'DTT'],
               ['印第安纳', '圣路易', '明尼亚玻利', '堪萨斯城', '休斯顿', '达拉斯', '新奥尔良', '俄克拉何马城',
                '亚特兰大', '迈阿密', '吐桑', '小岩石城', '辛辛那提', '丹佛', '凤凰城', '盐湖城', '拉斯韦加斯',
                '阿波寇尔喀', '波特兰', '旧金山', '洛杉矶', '西雅图', '安克拉治', '关岛', '奥兰多', '圣荷西',
                '圣安东尼', '米尔瓦基', '巴尔的摩', '夏威夷', '温哥华', '多伦多', '渥太华', '蒙特娄', '温尼伯',
                '卡加立', '爱德顿', '干达', '哈立法克斯', '开罗', '开普敦', '贝鲁特', '台拉维夫', '大马士革',
                '安曼', '吉达', '巴林', '约翰内斯堡', '金沙萨', '马耳他', '突尼斯', '达喀尔', '班吉', '布拉扎维',
                '毛里求斯', '杜拜', '科威特', '巴格达', '德黑兰', '地黎波斯', '阿尔吉尔', '卡萨马达卡', '拉斯马巴斯',
                '科那克里', '弗里敦', '巴马科', '阿比让', '蒙罗维亚', '尼亚美', '阿克拉', '瓦加杜古', '拉米堡',
                '亚恩德', '科多努', '拉哥斯', '自由府', '卢旺达', '温黎克', '卡吐穆', '伊斯坦堡', '安卡拉', '亚丁',
                '马斯开特', '阿巴具', '塔那那次棉', '爱丁堡', '洛梅', '马基鲁', '马基尼', '多哈', '达兰', '利雅得',
                '利隆圭', '恩将纳', '达来撤兰', '露沙卡', '摩加迪修', '恩特比', '坎帕拉', '阿迪斯阿鲁巴', '奈洛彼',
                '布兰太', '鲁伦素马凯斯', '索斯伯里', '达尔文', '伯斯', '悉尼', '布里斯本', '堪培拉', '墨尔本',
                '基督城', '惠灵顿', '奥克兰', '努美亚', '南地', '巴哥巴哥', '凯恩斯', '何巴特', '摩勒斯比港', '苏瓦',
                '大溪地',
                '特拉维夫', '布加勒斯特', '班加罗尔', '基辅', '索菲亚', '蒙得维的亚', '胡志明市', '内罗毕', '金奈',
                '布里斯班', '卡萨布兰卡', '麦纳麦', '珀斯', '安特卫普', '鹿特丹', '拉各斯', '里加', '圣迭戈',
                '伊斯兰堡', '伯明翰', '阿拉木图', '卡尔加里',
                'PIT', 'CLE', 'BUF', 'IND', 'STL', 'MSP', 'MKC', 'DFW', 'ORLEANS', 'MSY', 'OKC', 'MIA',
                'TUS', 'ROCK', 'LIT', 'DEN', 'PHX', 'LAKE', 'SLC', 'LAS', 'PDX', 'FRANCISCO', 'SFO', 'LAX', 'ANC',
                'GUM', 'ORL', 'JOSE', 'SJC', 'SAT', 'MTN', 'HNL', 'YVR', 'YYZ', 'YOW', 'YMQ', 'YMG', 'YYC', 'YEA',
                'YQX', 'YHZ', 'CAI', 'CPT', 'BEY', 'AVIV', 'TLV', 'AMM', 'JED', 'BAH', 'NFABURG', 'JNB', 'MLA',
                'TUN', 'DKR', 'BGF', 'BZV', 'MRU', 'DXB', 'KWI', 'BGW', 'THR', 'TIP', 'ALG', 'CAS', 'LPA', 'CKY',
                'FNA', 'BKO', 'ABJ', 'MLW', 'NIM', 'ACC', 'OUA', 'LAMY', 'FTL', 'COO', 'LOS', 'LVB', 'DA', 'LAD',
                'KRT', 'IST', 'ANK', 'ADE', 'MCT', 'ABD', 'TNR', 'EDI', 'LFW', 'MSU', 'MTS', 'DOH', 'DHA', 'RUH',
                'LLW', 'NDJ', 'ES', 'DAR', 'MGO', 'EBB', 'EBB', 'ABABA', 'ADD', 'BLZ', 'MAROUES', 'LUM', 'DRW',
                'PER', 'SYD', 'BNE', 'CBR', 'MEB', 'CHC', 'WLG', 'AKL', 'NOU', 'NAN', 'APGO', 'PPG', 'ALBATIN',
                'HBT', 'POM', 'PPT']
                ]

locationDict_en = [
                  ['Beijing', 'Shanghai', 'Tianjin', 'Xian', 'Hangchow', 'Dalian', 'Tsingtao', 'Foochow', 'Xiamen',
                   'Kunming', 'Nanking', 'Swatow', 'Guilin', 'Chengtu', 'Canton', 'Haikou', 'Changsha', 'Yantai',
                   'Chongqing', 'Wenzhou', 'Sanya', 'Harbin', 'Shengzhen', 'Nanchang', 'Honkkong', 'Macao', 'Taipei',
                   'Kaohsiung', 'Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Okinawa', 'Seoul', 'Pusan',
                   'Singapore', 'Kuala_Lunpur', 'Penang', 'Ipoh', 'Bangkok', 'Cnx', 'Phuket', 'Kuching', 'Jakarta',
                   'Denpasar', 'Medan', 'Palembang', 'Surabaya', 'Rangoon', 'Hanoi', 'Phnom_Penh', 'Saigon',
                   'Vientiane', 'Manila', 'Cebu', 'Dili', 'Kota_Kinabalu', 'Dacca', 'Sibu', 'Saipan',
                   'Bander_Seri_Begawan', 'Delhi', 'Kabul', 'Chittagon', 'Karachi', 'Tonggatapu', 'Nauru', 'Baguio',
                   'Bombay', 'Colomba', 'Calcutta', 'Madras', 'Kathmandu', 'Mexico_City', 'San_Salvador', 'Panama_City',
                   'Havana', 'Bogota', 'Quito', 'Lima', 'Santiago', 'Buends_Aires', 'San_Paulo', 'Rio_De_Janeiro',
                   'Brassilia', 'Caracas', 'Cayenne', 'Montebideo', 'Managua', 'Guatemala', 'Santo_Domingo', 'La_Paz',
                   'Kingston', 'San_Juan', 'Port_Au_Prince', 'Montego_Bay', 'San_Jose', 'Tegucigalpa_Tgu',
                   'Acapucco_Aca', 'Bridge_Town', 'Port_of_Spain', 'Asuncion', 'Manaus', 'Recife', 'Paramaribo',
                   'George_Town', 'London', 'Paris', 'Geneva', 'Zurich', 'Berlin', 'Hamberg', 'Frankfurt', 'Cologne',
                   'Munich', 'Dublin', 'Shannon', 'Warsaw', 'Amsterdam', 'Brussels', 'Vienna', 'Prague', 'Budapest',
                   'Athens', 'Milan', 'Rome', 'Barcelona', 'Bonn', 'Dussdolf', 'Stuttgart', 'Edinburgh', 'Sofia',
                   'Istanbul', 'Lisbon', 'Madrid', 'Gibraltar', 'Belgrade', 'Bucharest', 'Manchester', 'Copenhagen',
                   'Oslo', 'Stockholm', 'Helsinki', 'Glasgow', 'Nice', 'Newyork', 'Philadelphia', 'Boston',
                   'Washington', 'Chicago', 'Detroit', 'Pittsburgh', 'Cleveland', 'Buffalo',
                   'PEK', 'SHA', 'TSN', 'SIA', 'HGH', 'DLC', 'TAO', 'FOC', 'XMN', 'KMG', 'NKG', 'SWA', 'KWL', 'CTU',
                   'HAK', 'CSX', 'YNT', 'CKG', 'WNZ', 'SYX', 'HRB', 'SZX', 'KHN', 'HKG', 'MFM', 'TPE', 'KHH',
                   'TYO', 'OSA', 'NGO', 'SPK', 'FUK', 'OKA', 'SEL', 'PUS', 'SIN', 'KUL', 'PEN', 'IPH', 'BKK', 'HKT',
                   'KCH', 'JKT', 'DPS', 'MES', 'PLM', 'SUB', 'RGN', 'HAN', 'PENH', 'PNH', 'VTE', 'MNL', 'CEB', 'DIL',
                   'KINABALU', 'BKI', 'SBW', 'SPN', 'SERI', 'BWN', 'KBL', 'CGP', 'KHI', 'TBU', 'INU', 'BAG', 'BOM',
                   'CMB', 'CCU', 'MAA', 'KTM', 'MEX', 'SAL', 'PTY', 'UIO', 'LIM', 'SCL', 'SAN', 'AIRES',
                   'BUE', 'SAO', 'RIO', 'CCS', 'CAY', 'MVD', 'MGA', 'GUA', 'DOMINGO', 'SDQ', 'LPB', 'JUAN', 'SJU',
                   'PAP', 'MBJ', 'SJO', 'ACA', 'TOWN', 'BGI', 'POS', 'MAO', 'REL', 'PBM', 'TOWN', 'GRG', 'PAR', 'GVA',
                   'ZRH', 'BER', 'HAM', 'FRA', 'CGN', 'MUC', 'DUB', 'SNN', 'WAW', 'AMS', 'BRU', 'VIE', 'PRG', 'BUD',
                   'ATH', 'MIL', 'ROM', 'BCN', 'BNJ', 'DUS', 'STR', 'EDI', 'SOF', 'IST', 'LIS', 'MAD', 'GIB', 'BEG',
                   'BUH', 'MAN', 'CPH', 'OSL', 'STO', 'HEL', 'GLA', 'NCE', 'NYK', 'PHL', 'BOS', 'CHI', 'DTT'],
                  ['Indianapolis',
                   'St.Louis', 'Minneapolis', 'Kansas_City', 'Huston', 'Dalas', 'New_Orleans', 'Oklahoma_City',
                   'Atlanta', 'Miami', 'Tucson', 'Little_Rock', 'Cincinnati', 'Denver', 'Phoenix', 'Salt_Lake_City',
                   'Las_Vegas', 'Albuoerque', 'Portland', 'San_Francisco', 'Los_Angeles', 'Seattle', 'Anchorage',
                   'Guam', 'Orlando', 'San_Jose', 'San_Antonio', 'Milwakee', 'Baltimore', 'Honolulu', 'Vancouver',
                   'Toronto', 'Ottawa', 'Montreal', 'Winnipeg', 'Calgary', 'Edmonton', 'Gander', 'Halifax', 'Cairo',
                   'Capetown', 'Beirut', 'Tel_Aviv', 'Danascus', 'Amman', 'Jeddah', 'Bahrain', 'Johan_Nfaburg',
                   'Kinshasa', 'Malta', 'Tunis', 'Dakar', 'Ban-Gui', 'Braxxabille', 'Mauritius', 'Dubai', 'Kuwait',
                   'Baghdad', 'Tehran', 'Tripoli', 'Algiers', 'Casablanca', 'Laspalmas', 'Conakry', 'Freetown',
                   'Bamako', 'Abidjan', 'Monrovia', 'Niamey', 'Accra', 'Ouagadougou', 'Fort_Lamy', 'Yaounde', 'Cotonou',
                   'Lagos', 'Libreville', 'Luan_Da', 'Windhoek', 'Khartoum', 'Istanbul', 'Ankara', 'Aden', 'Muscat',
                   'Abadan', 'Tananarive', 'Edinburgh', 'Lome', 'Maseru', 'Manzini', 'Doha', 'Dhahran', 'Riyadh',
                   'Lilongwe', 'N\'djamena', 'Dar_Es_Salaam', 'Lusaka', 'Mogadishu', 'Entebbe', 'Kampala',
                   'Addis_Ababa', 'Nairobi', 'Blantyre', 'Lourenco_Maroues', 'Salisbury', 'Darwin', 'Perth', 'Sydney',
                   'Brisbane', 'Canberra', 'Melbourne', 'Christchurch', 'Wellington', 'Auckland', 'Noumea', 'Nadi',
                   'Pago_Apgo', 'Cairns', 'Hafr_Albatin', 'Potr_Moresby', 'Suva', 'Papeete',
                   'Tel_Aviv', 'Bucharest', 'Bangalore', 'Kyiv', 'Sofia', 'Montevideo', 'Ho_Chi_Minh_City',
                   'Nairobi', 'Chennai', 'Brisbane', 'Casablanca', 'Manama', 'Perth', 'Antwerp', 'Rotterdam',
                   'Lagos', 'Riga', 'San_Diego', 'Islamabad', 'Birmingham', 'Alma-Ata', 'Calgary',
                   'PIT', 'CLE', 'BUF', 'IND', 'STL', 'MSP', 'MKC', 'DFW', 'ORLEANS', 'MSY', 'OKC', 'MIA',
                   'TUS', 'ROCK', 'LIT', 'DEN', 'PHX', 'LAKE', 'SLC', 'LAS', 'PDX', 'FRANCISCO', 'SFO', 'LAX', 'ANC',
                   'GUM', 'ORL', 'JOSE', 'SJC', 'SAT', 'MTN', 'HNL', 'YVR', 'YYZ', 'YOW', 'YMQ', 'YMG', 'YYC', 'YEA',
                   'YQX', 'YHZ', 'CAI', 'CPT', 'BEY', 'AVIV', 'TLV', 'AMM', 'JED', 'BAH', 'NFABURG', 'JNB', 'MLA',
                   'TUN', 'DKR', 'BGF', 'BZV', 'MRU', 'DXB', 'KWI', 'BGW', 'THR', 'TIP', 'ALG', 'CAS', 'LPA', 'CKY',
                   'FNA', 'BKO', 'ABJ', 'MLW', 'NIM', 'ACC', 'OUA', 'LAMY', 'FTL', 'COO', 'LOS', 'LVB', 'DA', 'LAD',
                   'KRT', 'IST', 'ANK', 'ADE', 'MCT', 'ABD', 'TNR', 'EDI', 'LFW', 'MSU', 'MTS', 'DOH', 'DHA', 'RUH',
                   'LLW', 'NDJ', 'ES', 'DAR', 'MGO', 'EBB', 'EBB', 'ABABA', 'ADD', 'BLZ', 'MAROUES', 'LUM', 'DRW',
                   'PER', 'SYD', 'BNE', 'CBR', 'MEB', 'CHC', 'WLG', 'AKL', 'NOU', 'NAN', 'APGO', 'PPG', 'ALBATIN',
                   'HBT', 'POM', 'PPT']
                   ]

roomtypeDict_ch = ['单人间', '双人间', '三人间', '大床房', '标准间', '商务间',
                   '单人间', '双人间', '三人间', '大床房', '标准间', '商务间',
                   '单人间', '双人间', '三人间', '大床房', '标准间', '商务间',
                   '经济间', '豪华间', '总统套房', '商务标准间', '家庭套间', '商务行政房', '商务套房', '豪华套房',
                   '商务间'
                   ]

roomcountDict_ch = ['一间', '二间', '两间', '三间', '四间', '五间', '六间', '七间', '八间', '九间', '十间'
                    ]

roomtypeDict_en = ['single', 'double', 'triple:', 'quad', 'queen', 'king',
                   'twin', 'double-double', 'studio', 'mini-suite', 'suite'
                   ]

roomcountDict_en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'
                    ]
