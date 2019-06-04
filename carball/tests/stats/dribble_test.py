import unittest

from carball.analysis.events.carry_detection import CarryDetection, CarryData
from carball.analysis.analysis_manager import AnalysisManager

from carball.tests.utils import run_analysis_test_on_replay, get_specific_replays, get_raw_replays, get_multiple_answers


class FakeIndex:

    def __init__(self, list):
        class FakeList:
            def tolist(self):
                return list
        self.values = FakeList()


class DribbleTests(unittest.TestCase):

    def test_dribble_detection_more_than_zero(self):

        def test(analysis: AnalysisManager, dribbles, flicks):
            proto_game = analysis.get_protobuf_data()
            carries = proto_game.game_stats.ball_carries
            self.assertGreater(len(carries), 0)
            player = proto_game.players[0]
            self.assertEqual(player.stats.ball_carries.total_carries, dribbles)
            self.assertEqual(player.stats.ball_carries.total_flicks, flicks)
            self.assertGreater(player.stats.ball_carries.total_carry_time, 0)

        run_analysis_test_on_replay(test, get_specific_replays()["DRIBBLES"], answers=get_multiple_answers(["DRIBBLES", "FLICKS"]))

    def test_dribble_detection_is_zero(self):

        def test(analysis: AnalysisManager):
            proto_game = analysis.get_protobuf_data()
            carries = proto_game.game_stats.ball_carries
            self.assertEqual(len(carries), 0)

        run_analysis_test_on_replay(test, get_specific_replays()["ZERO_DRIBBLE"])

    def test_total_dribble_time(self):
        def test(analysis: AnalysisManager):
            proto_game = analysis.get_protobuf_data()
            player = proto_game.players[0]
            print(player)

            percent = 2.705
            self.assertAlmostEqual(player.stats.ball_carries.total_carry_time, 196, delta=196 * percent / 100)

        run_analysis_test_on_replay(test, get_raw_replays()["SKYBOT_DRIBBLE_INFO"])

    def test_zero_dribbles(self):
        def test(analysis: AnalysisManager):
            proto_game = analysis.get_protobuf_data()
            carries = proto_game.game_stats.ball_carries
            self.assertEqual(len(carries), 0)

        run_analysis_test_on_replay(test, get_raw_replays()["KICKOFF_NO_TOUCH"])


    def test_dribble_merge_simple(self):
        overall_carry = CarryData([],
                                  FakeIndex([188, 257, 551, 681, 721, 745, 759, 823, 1445]),  # overall start
                                  FakeIndex([254, 264, 679, 719, 742, 756, 820, 829, 1551]))  # overall end
        player_carry = CarryData([],
                                 FakeIndex([188, 568, 603, 608, 1465]),  # player start
                                 FakeIndex([222, 596, 603, 619, 1537]))  # player end
        CarryDetection().merge_carries(overall_carry, player_carry)

        self.assertEqual(len(player_carry.start_frames), 3)
        self.assertEqual(len(player_carry.end_frames), 3)


    def test_dribble_merge_complex(self):
        overall_carry = CarryData([],
                                  FakeIndex([184, 239, 248, 330, 379, 404, 419, 444, 524, 562, 596, 612, 623, 762, 786, 818, 833, 1014, 1107, 1185, 1203, 1212, 1388, 1454, 1465, 1818, 1832, 1855, 1903, 1975, 2023, 2043, 2056, 2388, 2400, 2498, 2518, 2558, 2687, 2919, 2995, 3017, 3031, 3035, 3119, 3190, 3365, 3385, 3414, 3486, 3568, 3590, 3636, 3664, 3681, 3692, 3789, 3827, 3941, 3964, 3997, 4020, 4034, 4054, 4153, 4212, 4231, 4245, 4271, 4357, 4376, 4467, 4480, 4557, 4608, 4670, 4750, 4830, 4919, 4988, 5011, 5015, 5093, 5169, 5215, 5609, 5637, 5681, 5701, 5715, 6009, 6040, 6060, 6122, 6213, 6564, 6596, 6616, 6682, 6778, 6794, 6868, 6882, 6920, 7001, 7034, 7048, 7096, 7120, 7137, 7150, 7219, 7299, 7317, 7327, 7420, 7443, 7477, 7513, 7613, 7686, 7697, 7808, 7881, 7942, 7958, 7988, 8041, 8070, 8090, 8129, 8150, 8257, 8311, 8400, 8419, 8468, 8762, 8774, 8788, 8802, 8815, 8879, 8942, 9227, 9281, 9367, 9450, 9598, 9613, 9637, 9651, 9683, 9732, 9784, 9892, 10293, 10301, 10408, 10424, 10434, 10458, 10562, 10756, 10776, 10799, 10815, 10958, 10979, 10998, 11020, 11034, 11129, 11146, 11229, 11337, 11456, 11482, 11506, 11520, 11578, 11696, 11712, 11792, 11835, 11851, 11857, 11929, 11977, 11997, 12047, 12158, 12368, 12383, 12435, 12517, 12907, 12940, 12960, 13010, 13096, 13563, 13624, 13660, 13743, 13756, 13761, 13844, 13928, 13953, 13970, 14059, 14123, 14208, 14256, 14336, 14350, 14414, 14480, 14793, 14872, 14888, 14978, 15001, 15015, 15047, 15123, 15157, 15178, 15240, 15349, 15364, 15397, 15429, 15481, 15558, 15585, 15601, 15641, 15744, 15804, 15852, 15872, 15906, 15920, 15950, 15995, 16022, 16039, 16059, 16258, 16282, 16297, 16425, 16482, 16504, 16696, 16769, 16951, 17068, 17221, 17231, 17302, 17323, 17336, 17359, 17442, 17519, 17537, 17567, 17664, 17678, 17745, 17782, 17796, 18179, 18238, 18247, 18325, 18381, 18405, 18427, 18472, 18510, 18524, 18544, 18606, 18623, 18744, 18877, 19158, 19210, 19256, 19277, 19588, 19608, 19627, 19669, 19705, 19856, 19877, 19891, 19985, 20069, 20126, 20188, 20260, 20385, 20399, 20432, 20540, 20604, 20626, 20748, 20767, 20795, 21049, 21083, 21103, 21117, 21149, 21269, 21635, 21706, 21774, 21807, 21826, 21868, 21948, 21995, 22009, 22067, 22138, 22162, 22170, 22206, 22226, 22240, 22247, 22277, 22380, 22448, 22471, 22489, 22553, 22659, 22976, 23006, 23025, 23036, 23054, 23127, 23248, 23262, 23335, 23355, 23400, 23428, 23683, 23718, 23739, 23754, 23778, 23898, 24181, 24365, 24435, 24614, 24631, 24649, 24662, 24706, 24820, 25192, 25206, 25219, 25250, 25321, 25374, 25489, 25495, 25546, 25645, 25674, 25708, 26102, 26165, 26174, 26242, 26260, 26544, 26579, 26601, 26663, 26745, 26892, 26910, 27180, 27210, 27228, 27299, 27380, 27440, 27460, 27543, 27593, 27674, 27695, 27709, 27731, 27763, 27802, 27820, 27850, 27975, 27986, 28042, 28110, 28137, 28162, 28175, 28199, 28202, 28258, 28280, 28332, 28507, 28526, 28583, 28845, 28915, 28944, 29007, 29078, 29090, 29201, 29468, 29477, 29507, 29603, 29707, 29739, 30064, 30125, 30135, 30204, 30222, 30495, 30549, 30684, 30777, 30823, 30853, 30871, 30908, 30931, 31030, 31098, 31332, 31358, 31460, 31833, 31878, 31905, 32168, 32201, 32221, 32276, 32392, 32409, 32478, 32573, 32587, 32635, 32763, 32821, 32869, 33322, 33336, 33460, 33517, 33756, 33769, 33778, 33861, 33927, 33957, 33972, 34017, 34056, 34224, 34256, 34280, 34293, 34344, 34431, 34465, 34485, 34498, 34508, 34596, 34617, 34685, 34718, 34751, 34765, 34800, 34949, 34964, 35109, 35332, 35347, 35658, 35713, 35800, 35821, 35921, 35962, 35983, 36150, 36309, 36322, 36351, 36612, 36650, 36671, 36685, 36704, 36739, 36759, 36775, 36810, 36878, 36916, 36939, 36953, 36968, 37082, 37265, 37282, 37330, 37596, 37628, 37647, 37709, 37801, 37833, 37877, 37892, 37899, 37920, 38025, 38048, 38063, 38089, 38411, 38442, 38461, 38533, 38592, 38649, 38701, 38721, 38788, 38873, 38915, 38955, 38973, 39141, 39159, 39174, 39379, 39395, 39456, 39538, 39687, 39742, 39808, 39831, 39891, 39916, 39931, 39940, 39961, 40031, 40170, 40184, 40235, 40250, 40259, 40263, 40284, 40334, 40347, 40381, 40439, 40702, 40719, 40805, 40906, 40941, 40960]),  # overall start
                                  FakeIndex([190, 246, 263, 377, 401, 415, 424, 522, 559, 593, 608, 615, 760, 784, 815, 829, 836, 1029, 1182, 1199, 1209, 1365, 1391, 1457, 1815, 1828, 1835, 1879, 1923, 2021, 2041, 2052, 2058, 2398, 2496, 2515, 2526, 2601, 2915, 2927, 3015, 3027, 3033, 3054, 3188, 3363, 3382, 3393, 3483, 3531, 3588, 3634, 3661, 3677, 3686, 3787, 3824, 3907, 3962, 3994, 4017, 4030, 4037, 4151, 4209, 4229, 4240, 4245, 4286, 4374, 4464, 4476, 4495, 4606, 4668, 4747, 4757, 4849, 4986, 5008, 5012, 5022, 5156, 5195, 5607, 5634, 5678, 5699, 5710, 5716, 6038, 6057, 6068, 6149, 6310, 6594, 6613, 6624, 6713, 6792, 6865, 6878, 6884, 6951, 7032, 7045, 7094, 7118, 7133, 7142, 7157, 7289, 7313, 7323, 7416, 7441, 7451, 7484, 7516, 7684, 7695, 7805, 7823, 7939, 7954, 7962, 8016, 8068, 8087, 8098, 8147, 8158, 8277, 8350, 8417, 8466, 8503, 8771, 8783, 8788, 8810, 8816, 8896, 8959, 9233, 9304, 9436, 9595, 9609, 9634, 9646, 9651, 9706, 9776, 9890, 9957, 10298, 10405, 10421, 10429, 10437, 10496, 10754, 10772, 10795, 10802, 10821, 10976, 10994, 11017, 11029, 11036, 11131, 11163, 11335, 11454, 11480, 11503, 11515, 11521, 11609, 11710, 11790, 11833, 11847, 11855, 11889, 11975, 11994, 12005, 12062, 12366, 12379, 12386, 12471, 12655, 12938, 12957, 12967, 13046, 13310, 13622, 13658, 13740, 13751, 13756, 13825, 13888, 13951, 13966, 13975, 14076, 14200, 14253, 14334, 14346, 14411, 14433, 14534, 14808, 14886, 14976, 14998, 15011, 15017, 15121, 15155, 15175, 15238, 15346, 15360, 15368, 15427, 15456, 15516, 15583, 15598, 15606, 15742, 15802, 15850, 15869, 15880, 15915, 15921, 15993, 16020, 16035, 16044, 16256, 16279, 16293, 16300, 16444, 16502, 16694, 16734, 16902, 17066, 17218, 17229, 17300, 17320, 17332, 17356, 17370, 17457, 17523, 17565, 17661, 17674, 17716, 17779, 17792, 17798, 18184, 18245, 18262, 18379, 18403, 18424, 18459, 18508, 18520, 18526, 18603, 18620, 18629, 18825, 19156, 19208, 19253, 19273, 19288, 19605, 19622, 19628, 19674, 19854, 19875, 19886, 19897, 20002, 20124, 20186, 20212, 20382, 20395, 20402, 20457, 20602, 20624, 20746, 20764, 20774, 20797, 21081, 21100, 21112, 21117, 21189, 21633, 21665, 21772, 21805, 21822, 21833, 21946, 21992, 22005, 22012, 22083, 22158, 22164, 22203, 22223, 22235, 22241, 22275, 22305, 22446, 22468, 22483, 22489, 22609, 22974, 23004, 23021, 23032, 23050, 23059, 23167, 23260, 23333, 23353, 23398, 23423, 23428, 23716, 23737, 23749, 23755, 23823, 24179, 24348, 24407, 24612, 24627, 24636, 24657, 24662, 24716, 24933, 25204, 25216, 25246, 25254, 25354, 25486, 25490, 25496, 25643, 25671, 25706, 25797, 26108, 26172, 26190, 26258, 26284, 26576, 26587, 26607, 26713, 26889, 26907, 26916, 27208, 27225, 27235, 27331, 27438, 27458, 27466, 27547, 27672, 27693, 27705, 27711, 27761, 27799, 27817, 27826, 27863, 27984, 28006, 28108, 28135, 28158, 28171, 28177, 28199, 28221, 28278, 28330, 28505, 28524, 28534, 28591, 28913, 28942, 28979, 29075, 29083, 29199, 29209, 29474, 29494, 29507, 29625, 29736, 29797, 30070, 30133, 30150, 30220, 30235, 30546, 30557, 30697, 30821, 30850, 30867, 30877, 30912, 31027, 31059, 31330, 31355, 31375, 31580, 31876, 31902, 31915, 32199, 32218, 32229, 32331, 32407, 32468, 32570, 32583, 32590, 32656, 32798, 32826, 33062, 33334, 33351, 33496, 33753, 33766, 33773, 33795, 33925, 33954, 33969, 33977, 34035, 34222, 34254, 34277, 34289, 34295, 34351, 34463, 34482, 34494, 34499, 34594, 34614, 34683, 34716, 34749, 34761, 34767, 34946, 34960, 34968, 35330, 35344, 35351, 35663, 35736, 35819, 35870, 35942, 35970, 36030, 36306, 36318, 36324, 36353, 36648, 36668, 36680, 36687, 36736, 36757, 36771, 36776, 36862, 36914, 36936, 36949, 36956, 36992, 37262, 37279, 37286, 37336, 37625, 37644, 37654, 37738, 37830, 37874, 37888, 37895, 37917, 38023, 38046, 38059, 38066, 38090, 38439, 38457, 38467, 38563, 38629, 38699, 38716, 38722, 38809, 38913, 38952, 38970, 39139, 39155, 39165, 39377, 39392, 39400, 39500, 39684, 39695, 39803, 39809, 39889, 39913, 39928, 39936, 39943, 39981, 40167, 40180, 40187, 40247, 40255, 40261, 40269, 40304, 40343, 40349, 40436, 40443, 40716, 40733, 40904, 40938, 40958, 40968]))  # overall end
        player_carry = CarryData([],
                                 FakeIndex([185, 498, 576, 628, 662, 1116, 1246, 1555, 1573, 1670, 2407, 2597, 2692, 2709, 3215, 3245, 3451, 3494, 4173, 4410, 4564, 4927, 5218, 5266, 5339, 5407, 6009, 6213, 6240, 6564, 7006, 7057, 7892, 8329, 9228, 9469, 9754, 9795, 9873, 9906, 10313, 10470, 10572, 10587, 10735, 10737, 11229, 11733, 11811, 11929, 12168, 12179, 12523, 12560, 12575, 12907, 13110, 13181, 13563, 13761, 13866, 13942, 14351, 14380, 14480, 14511, 14796, 14948, 15254, 16062, 16507, 16573, 16851, 17013, 17093, 17264, 17603, 18179, 18576, 18802, 18877, 19051, 19091, 19183, 19758, 20115, 20138, 20272, 20540, 20689, 21049, 21278, 21295, 21434, 21475, 21978, 22182, 22380, 22589, 22597, 22664, 22695, 22930, 23319, 23683, 23900, 23940, 24011, 24201, 24457, 24820, 25410, 25607, 25656, 25748, 26102, 26565, 26705, 26807, 27180, 27398, 27418, 27656, 28203, 28345, 28385, 28409, 28845, 29028, 29090, 29707, 29746, 30065, 30499, 30512, 30787, 31042, 31166, 31468, 31833, 32168, 32878, 33531, 33577, 34134, 34581, 34881, 35172, 35659, 36018, 36150, 36187, 36617, 36628, 37153, 37596, 37801, 37842, 37966, 38411, 38612, 38668, 38875, 38921, 38997, 39087, 39110, 39118, 39217, 39541, 39653, 40409, 40440, 40836]),  # player start
                                 FakeIndex([187, 501, 577, 657, 676, 1173, 1324, 1559, 1637, 1808, 2470, 2600, 2704, 2782, 3217, 3337, 3477, 3528, 4198, 4453, 4575, 4934, 5250, 5337, 5387, 5555, 6009, 6233, 6303, 6564, 7019, 7060, 7925, 8334, 9230, 9580, 9768, 9857, 9880, 9928, 10395, 10470, 10583, 10729, 10735, 10741, 11292, 11759, 11822, 11972, 12176, 12355, 12538, 12568, 12650, 12907, 13141, 13310, 13565, 13805, 13873, 13947, 14374, 14401, 14504, 14521, 14797, 14958, 15336, 16228, 16515, 16656, 16884, 17021, 17210, 17291, 17654, 18180, 18587, 18819, 19009, 19062, 19119, 19184, 19771, 20119, 20168, 20372, 20557, 20699, 21049, 21285, 21364, 21438, 21622, 21984, 22185, 22418, 22591, 22604, 22679, 22923, 22932, 23323, 23683, 23914, 24007, 24147, 24289, 24595, 24914, 25412, 25611, 25661, 25753, 26104, 26570, 26708, 26880, 27181, 27413, 27424, 27665, 28206, 28345, 28393, 28476, 28846, 29056, 29188, 29722, 29785, 30066, 30502, 30539, 30790, 31045, 31292, 31568, 31834, 32168, 33062, 33545, 33745, 34170, 34583, 34889, 35318, 35661, 36026, 36162, 36298, 36617, 36642, 37253, 37596, 37820, 37861, 38000, 38411, 38616, 38692, 38894, 38921, 39067, 39091, 39113, 39129, 39359, 39609, 39678, 40430, 40440, 40848]))  # player end
        CarryDetection().merge_carries(overall_carry, player_carry)

        self.assertEqual(len(player_carry.start_frames), 133)
        self.assertEqual(len(player_carry.end_frames), 133)

    def test_dribble_merge_rumble(self):
        overall_carry = CarryData([],
                                  FakeIndex([187, 283, 338, 516, 621, 638, 722, 745, 758, 1116, 1237, 1541, 1584, 1851, 1926, 1948, 2013, 2036, 2051, 2174, 2349, 2394, 2409, 2439, 2741, 2803, 2887, 3011, 3094, 3118, 3136, 3152, 3187, 3325, 3343, 3400, 3444, 3464, 3517, 3587, 3701, 3833, 4175, 4195, 4242, 4395, 4409, 4518, 4542, 4559, 4566, 4694, 4994, 5067, 5171, 5336, 5402, 5682, 5701, 5749, 5834, 5851, 5927, 5952, 6021, 6053, 6231, 6243, 6328, 6424, 6457, 6569, 6590, 6650, 6680, 6821, 6929, 6938, 7023, 7144, 7293, 7308, 7442, 7535, 7603, 7633, 7650, 7727, 7732, 7801, 7907, 7938, 8091, 8109, 8153, 8177, 8194, 8201, 8508, 8567, 8685, 8709, 8799, 8870, 9009, 9241, 9288, 9297, 9393, 9883, 10016, 10033, 10187, 10229, 10347, 10469, 10626, 10642, 10692, 10784, 10809, 10880, 10955, 11038, 11138, 11262, 11556, 11598]),  # overall start
                                  FakeIndex([280, 308, 444, 560, 636, 720, 741, 754, 759, 1176, 1269, 1573, 1721, 1852, 1945, 2010, 2033, 2047, 2053, 2184, 2391, 2406, 2415, 2470, 2800, 2838, 2899, 3044, 3115, 3133, 3149, 3160, 3323, 3340, 3350, 3442, 3461, 3469, 3585, 3603, 3702, 3843, 4185, 4239, 4276, 4407, 4515, 4539, 4553, 4560, 4603, 4718, 5003, 5168, 5198, 5356, 5407, 5698, 5710, 5766, 5849, 5863, 5950, 6018, 6051, 6083, 6241, 6325, 6421, 6433, 6534, 6588, 6648, 6677, 6782, 6876, 6935, 6952, 7070, 7205, 7305, 7439, 7533, 7600, 7630, 7647, 7724, 7730, 7799, 7905, 7935, 7983, 8106, 8149, 8175, 8190, 8198, 8204, 8530, 8647, 8707, 8754, 8867, 8888, 9037, 9244, 9295, 9310, 9517, 9893, 10031, 10063, 10226, 10246, 10364, 10545, 10640, 10689, 10740, 10806, 10877, 10953, 10977, 11136, 11189, 11286, 11596, 11630]))  # overall end
        player_carry = CarryData([],
                                 FakeIndex([1851, 3413, 3701, 4441, 6717, 10731, 11040]),  # player start
                                 FakeIndex([1852, 3414, 3702, 4441, 6718, 10731, 11040]))  # player end
        CarryDetection().merge_carries(overall_carry, player_carry)

        self.assertEqual(len(player_carry.start_frames), 7)
        self.assertEqual(len(player_carry.end_frames), 7)


if __name__ == '__main__':
    unittest.main()
