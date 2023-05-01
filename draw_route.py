import turtle

coords = "MULTILINESTRING ((149.065507 -35.41440300000001, 149.06528 -35.414126, 149.065251 -35.414092, 149.06519699999998 -35.414051, 149.06519600000001 -35.414049, 149.06516100000002 -35.414028, 149.06512 -35.414025, 149.06506399999998 -35.414034, 149.06504099999998 -35.414063, 149.065028 -35.414093, 149.065021 -35.414120000000004, 149.065026 -35.41415, 149.065071 -35.414248, 149.065675 -35.415063, 149.064496 -35.415664, 149.06301499999998 -35.416418, 149.06313 -35.416565000000006, 149.064352 -35.418185, 149.064649 -35.418581, 149.064851 -35.418848, 149.064991 -35.41903700000001, 149.06563300000002 -35.419874, 149.065852 -35.419763, 149.065914 -35.419746999999994, 149.06597 -35.419743, 149.066407 -35.41952, 149.067143 -35.419145, 149.06793000000002 -35.418743, 149.06886599999999 -35.418267, 149.06888899999998 -35.418232, 149.06891299999998 -35.418206, 149.06894599999998 -35.418177, 149.068984 -35.418152, 149.06938500000004 -35.417947999999996, 149.069667 -35.417806, 149.069858 -35.417709, 149.069888 -35.41769600000001, 149.069953 -35.417677000000005, 149.07003 -35.417673, 149.070729 -35.417316, 149.07185900000002 -35.416740999999995, 149.073391 -35.415960999999996, 149.073638 -35.415818, 149.073846 -35.415704999999996, 149.074188 -35.415434999999995, 149.074216 -35.415403000000005, 149.07425800000001 -35.415343, 149.074291 -35.41526900000001, 149.074309 -35.415192, 149.07431100000005 -35.415113, 149.074006 -35.414515, 149.07388999999998 -35.414271, 149.07378 -35.414026, 149.073675 -35.413778, 149.073576 -35.413529, 149.073483 -35.413278999999996, 149.073397 -35.413027, 149.07331499999998 -35.412773, 149.07323400000004 -35.412494, 149.073176 -35.412273, 149.073123 -35.41205, 149.07307600000001 -35.411826, 149.073036 -35.411602, 149.072997 -35.411331, 149.072972 -35.411105, 149.07294299999998 -35.410740000000004, 149.072931 -35.4104, 149.072931 -35.410121999999994, 149.072938 -35.409846, 149.072957 -35.409571, 149.072977 -35.409341, 149.073006 -35.409110999999996, 149.073047 -35.408837, 149.07308799999998 -35.408601000000004, 149.07314 -35.408356, 149.073148 -35.408318, 149.07320500000003 -35.408085, 149.073267 -35.407852, 149.073337 -35.40762, 149.07341200000002 -35.40739, 149.073528 -35.407069, 149.07407 -35.405659, 149.07417 -35.405365, 149.074246 -35.40511, 149.07429299999998 -35.404939, 149.074344 -35.404724, 149.074391 -35.404509999999995, 149.07443 -35.404293, 149.074457 -35.404119, 149.074481 -35.403921000000004, 149.07449900000003 -35.403721000000004, 149.074512 -35.403521000000005, 149.07451799999998 -35.403286, 149.074517 -35.40305, 149.074514 -35.402955, 149.074503 -35.402751, 149.07449 -35.402574, 149.074478 -35.402421999999994, 149.074453 -35.402183, 149.074397 -35.401831, 149.07433400000002 -35.401526000000004, 149.07426999999998 -35.401265, 149.07417 -35.40092, 149.074085 -35.400664, 149.073974 -35.400368, 149.073851 -35.400075, 149.073735 -35.399826000000004, 149.073675 -35.399703, 149.072259 -35.396951, 149.07199300000002 -35.396432, 149.071979 -35.396406, 149.071928 -35.396311, 149.071788 -35.396048, 149.07101 -35.394597, 149.070806 -35.394239, 149.070539 -35.393796, 149.070258 -35.393359000000004, 149.069964 -35.392928000000005, 149.069697 -35.392556, 149.069475 -35.392399, 149.06941799999998 -35.392365999999996, 149.069356 -35.392340000000004, 149.069278 -35.392317999999996, 149.069188 -35.392305, 149.069107 -35.392303000000005, 149.069026 -35.392312, 149.068677 -35.392495000000004, 149.068522 -35.392578, 149.068246 -35.392727, 149.067658 -35.393051, 149.067646 -35.393058, 149.06758100000002 -35.393095, 149.067052 -35.393396, 149.065903 -35.394073999999996, 149.065173 -35.394505, 149.06417 -35.395098, 149.06411 -35.395108, 149.063417 -35.395533, 149.06336000000002 -35.39557, 149.063233 -35.395647000000004, 149.06301399999998 -35.395782000000004, 149.062852 -35.39587, 149.06275600000004 -35.395922, 149.0625 -35.396049, 149.062313 -35.396128000000004, 149.06221599999998 -35.396165, 149.06209199999998 -35.396203, 149.061891 -35.396256, 149.06178899999998 -35.396279, 149.06166000000002 -35.396301, 149.06145 -35.396326, 149.061346 -35.396332, 149.06121399999998 -35.396336, 149.061107 -35.396336, 149.060976 -35.396330999999996, 149.060844 -35.396321, 149.06073999999998 -35.396308000000005, 149.060609 -35.396288, 149.060506 -35.396267, 149.06038 -35.396239, 149.060278 -35.396212, 149.06015600000003 -35.396172, 149.060058 -35.396139, 149.05986900000002 -35.396060999999996, 149.05977900000002 -35.396017, 149.059667 -35.395959000000005, 149.05947 -35.395841, 149.059412 -35.395828, 149.05938500000002 -35.395815999999996, 149.059354 -35.395798, 149.059327 -35.395776000000005, 149.059309 -35.395757, 149.059281 -35.395713, 149.059125 -35.395592, 149.058979 -35.395464000000004, 149.058842 -35.395329, 149.05871399999998 -35.395189, 149.058596 -35.395041, 149.058489 -35.394890000000004, 149.058393 -35.39473300000001, 149.058308 -35.394572, 149.05828799999998 -35.394528, 149.058267 -35.394483, 149.058228 -35.394389000000004, 149.058183 -35.394269, 149.058152 -35.394172, 149.058119 -35.39405, 149.05809299999999 -35.393927000000005, 149.058075 -35.393828000000006, 149.058061 -35.393703, 149.058053 -35.393603000000006, 149.05804799999999 -35.393478, 149.058049 -35.393378000000006, 149.058064 -35.393178000000006, 149.058073 -35.393125, 149.05809399999998 -35.39298, 149.05816299999998 -35.392663, 149.058222 -35.392424, 149.058299 -35.392137000000005, 149.058312 -35.392094, 149.058323 -35.392056, 149.058398 -35.391808000000005, 149.058479 -35.391562, 149.058578 -35.391277, 149.05866799999998 -35.391042, 149.058765 -35.390809000000004, 149.05886600000002 -35.390578000000005, 149.058952 -35.390394, 149.058974 -35.390347999999996, 149.059086 -35.390121, 149.05913 -35.389879, 149.059131 -35.389833, 149.05912000000004 -35.389787, 149.059101 -35.38975, 149.059074 -35.389717, 149.059033 -35.389683000000005, 149.058809 -35.389592, 149.058685 -35.389544, 149.058533 -35.389495000000004, 149.058378 -35.389451, 149.058192 -35.38941, 149.058002 -35.389379, 149.057837 -35.389359000000006, 149.057645 -35.389346, 149.05745100000001 -35.389343, 149.05725900000002 -35.38935, 149.057154 -35.389359000000006, 149.057067 -35.389366, 149.05687600000002 -35.389394, 149.05674199999999 -35.389419000000004, 149.056611 -35.389449000000006, 149.05648200000002 -35.389484, 149.056354 -35.389523, 149.05474300000003 -35.390097999999995, 149.054601 -35.390146, 149.05445500000002 -35.390184000000005, 149.05430900000002 -35.390218, 149.054158 -35.390243, 149.054033 -35.390257, 149.053907 -35.390268, 149.05379399999998 -35.390271999999996, 149.053779 -35.390273, 149.053678 -35.390273, 149.053549 -35.39026900000001, 149.053424 -35.39026, 149.053298 -35.390245, 149.053173 -35.390225, 149.053049 -35.3902, 149.052927 -35.39017, 149.052804 -35.390134, 149.052707 -35.390101, 149.05258700000002 -35.390057000000006, 149.052469 -35.390008, 149.052356 -35.389953999999996, 149.052269 -35.389907, 149.052166 -35.389845, 149.052092 -35.389798, 149.05193400000002 -35.389684, 149.051757 -35.389539, 149.051726 -35.389507, 149.051704 -35.389478999999994, 149.051682 -35.389443, 149.05166800000003 -35.389412, 149.05158799999998 -35.389331, 149.051513 -35.389246, 149.051438 -35.389153, 149.051431 -35.389145, 149.05134 -35.389023, 149.051253 -35.388897, 149.051173 -35.38877, 149.05111100000002 -35.388666, 149.051039 -35.388536, 149.05098600000002 -35.38843, 149.050923 -35.388295, 149.05086799999998 -35.388159, 149.050817 -35.388023, 149.05076499999998 -35.387859999999996, 149.050721 -35.387696000000005, 149.05068400000002 -35.38753, 149.05064299999998 -35.387297, 149.050602 -35.387038000000004, 149.050568 -35.386779, 149.050535 -35.386466999999996, 149.050514 -35.386208, 149.05049700000004 -35.385906, 149.050493 -35.385776, 149.050489 -35.385657, 149.050487 -35.385286, 149.050498 -35.384918, 149.050521 -35.384547999999995, 149.050556 -35.38418, 149.050603 -35.383811, 149.050644 -35.38357, 149.050677 -35.383413, 149.050709 -35.383288, 149.05078500000002 -35.383039000000004, 149.050843 -35.382877, 149.050907 -35.382715000000005, 149.05097800000001 -35.382554999999996, 149.05104 -35.382427, 149.051122 -35.382272, 149.051209 -35.382117, 149.05121 -35.382115, 149.051302 -35.381965, 149.051402 -35.381815, 149.05150600000002 -35.381668, 149.051593 -35.381552, 149.05170800000002 -35.381409999999995, 149.051827 -35.381271000000005, 149.051845 -35.381252, 149.051953 -35.381135, 149.052084 -35.381002, 149.052219 -35.380873, 149.052359 -35.380747, 149.052042 -35.380479, 149.05201100000002 -35.380444, 149.051988 -35.380396000000005, 149.051602 -35.380095000000004, 149.05154900000002 -35.380078000000005, 149.05149699999998 -35.380047, 149.05145500000003 -35.380007, 149.05142800000002 -35.379959, 149.05124600000002 -35.379816999999996, 149.05092 -35.379564, 149.050577 -35.379313, 149.050402 -35.379193, 149.05017800000002 -35.379045, 149.049952 -35.378899, 149.049722 -35.37876, 149.04943500000002 -35.378594, 149.049142 -35.378433, 149.048846 -35.37828, 149.048544 -35.378132, 149.048338 -35.378037, 149.048236 -35.377990999999994, 149.047926 -35.377857, 149.04761100000002 -35.37773, 149.047291 -35.377609, 149.04702900000004 -35.377579, 149.047011 -35.377584000000006, 149.046982 -35.377586, 149.04695800000002 -35.377582000000004, 149.04693999999998 -35.377576, 149.04691699999998 -35.377562, 149.046904 -35.37755, 149.04689199999999 -35.377528999999996, 149.046887 -35.377509, 149.046886 -35.377497, 149.04689199999999 -35.377474, 149.046906 -35.377452000000005, 149.046923 -35.377437, 149.04693500000005 -35.37743, 149.04711899999998 -35.377286, 149.04726200000002 -35.377077, 149.047441 -35.37683, 149.04759400000003 -35.376626, 149.047786 -35.376386, 149.04801899999998 -35.37611, 149.048495 -35.375581, 149.048673 -35.375374, 149.04885500000003 -35.375161999999996, 149.049704 -35.374119, 149.05088 -35.372695, 149.05078 -35.37267, 149.05068100000003 -35.372640999999994, 149.050603 -35.372614, 149.050509 -35.372575, 149.050347 -35.372495, 149.050197 -35.3724, 149.050119 -35.372341999999996, 149.05006 -35.372293000000006, 149.04998999999998 -35.372228, 149.049926 -35.372158, 149.049867 -35.372087, 149.049823 -35.372029, 149.04978300000002 -35.371968, 149.049743 -35.371893, 149.049681 -35.371747, 149.049655 -35.371664, 149.04963899999998 -35.371595, 149.04961799999998 -35.37146, 149.049613 -35.371373999999996, 149.049614 -35.371306, 149.049619 -35.37122, 149.04963 -35.371152, 149.049662 -35.371008, 149.049724 -35.37081, 149.049793 -35.370639000000004, 149.04986 -35.370495, 149.049923 -35.370378, 149.049991 -35.370262, 149.050065 -35.370149, 149.051001 -35.368885, 149.051067 -35.368790999999995, 149.051145 -35.368671, 149.051244 -35.368499, 149.051345 -35.368299, 149.051429 -35.368092000000004, 149.05149699999998 -35.367883, 149.05155 -35.367671, 149.05158600000001 -35.367487, 149.051605 -35.367356, 149.051619 -35.367225000000005, 149.051625 -35.367119, 149.051626 -35.366904, 149.051612 -35.366688, 149.051597 -35.366582, 149.051574 -35.36645, 149.051546 -35.366316000000005, 149.051518 -35.366211, 149.051485 -35.366107, 149.051445 -35.365990000000004, 149.05144099999998 -35.365978999999996, 149.051377 -35.365818, 149.051306 -35.365659, 149.051245 -35.36553200000001, 149.051164 -35.365375, 149.051095 -35.365253, 149.051003 -35.3651, 149.050906 -35.364951, 149.050803 -35.364804, 149.050649 -35.364602000000005, 149.050486 -35.36440700000001, 149.049685 -35.363515, 149.048746 -35.36247, 149.04863799999998 -35.362343, 149.048555 -35.36223900000001, 149.048454 -35.362107, 149.048361 -35.361971999999994, 149.048273 -35.361835, 149.048174 -35.361667, 149.04808400000002 -35.361496, 149.048015 -35.36135, 149.047952 -35.361204, 149.04789499999998 -35.361056, 149.047877 -35.361007, 149.047862 -35.36096, 149.047797 -35.360751, 149.04773899999998 -35.36050900000001, 149.047727 -35.360434999999995, 149.047697 -35.360265000000005, 149.047673 -35.360051, 149.047661 -35.359834, 149.04766 -35.359803, 149.04766 -35.359764, 149.047663 -35.359559999999995, 149.04767900000002 -35.35934, 149.047708 -35.359122000000006, 149.04774799999998 -35.35890500000001, 149.04779299999998 -35.35872, 149.047857 -35.358507, 149.047922 -35.358326, 149.04796299999998 -35.35823, 149.048009 -35.358118, 149.04810600000005 -35.357913, 149.048217 -35.357712, 149.04832 -35.357544, 149.048452 -35.357352, 149.048594 -35.357166, 149.048745 -35.356984999999995, 149.048885 -35.356834, 149.049006 -35.356713, 149.049258 -35.356474, 149.04930900000002 -35.356398999999996, 149.049377 -35.356313, 149.049507 -35.356188, 149.04953 -35.356165000000004, 149.049557 -35.356141, 149.04965900000002 -35.356044, 149.04968200000002 -35.356028, 149.049713 -35.356010999999995, 149.049769 -35.355993, 149.050468 -35.355334, 149.050469 -35.355313, 149.050479 -35.355288, 149.05050500000002 -35.355252, 149.050528 -35.355233, 149.050548 -35.355221, 149.050578 -35.355211, 149.050603 -35.355206, 149.051449 -35.354407, 149.051454 -35.354378000000004, 149.05146499999998 -35.35435, 149.051482 -35.354325, 149.051499 -35.354306, 149.051525 -35.354284, 149.05154900000002 -35.354271000000004, 149.05158 -35.354259000000006, 149.051615 -35.35425, 149.051705 -35.354167, 149.05196899999999 -35.353918, 149.051998 -35.35389, 149.05203 -35.353858, 149.052046 -35.353815999999995, 149.052075 -35.353772, 149.05229 -35.353567, 149.052311 -35.353552, 149.052338 -35.353536, 149.052367 -35.353522999999996, 149.052394 -35.353517, 149.05381 -35.352181, 149.055164 -35.350904, 149.055381 -35.350688, 149.055485 -35.350578000000006, 149.055609 -35.350439, 149.055738 -35.350286000000004, 149.05586200000002 -35.35013, 149.055981 -35.349971999999994, 149.05609400000003 -35.34981, 149.056202 -35.349646, 149.056303 -35.349478999999995, 149.0564 -35.349311, 149.05647199999999 -35.349174, 149.056497 -35.349127, 149.05651899999998 -35.349082, 149.056617 -35.348874, 149.056718 -35.348628999999995, 149.05681 -35.348383, 149.056878 -35.348168, 149.056948 -35.347910999999996, 149.056956 -35.347881, 149.056964 -35.347849, 149.05702 -35.347576000000004, 149.057048 -35.347402, 149.057068 -35.347263, 149.05708700000002 -35.347099, 149.057218 -35.345957, 149.057198 -35.345905, 149.057191 -35.345857, 149.057201 -35.345714, 149.05715800000002 -35.34555800000001, 149.05713400000002 -35.345522, 149.05709199999998 -35.34547, 149.057052 -35.345431, 149.056997 -35.34538700000001, 149.056939 -35.34535, 149.05308 -35.344346, 149.052984 -35.344319, 149.052651 -35.344218, 149.052275 -35.344092, 149.051906 -35.343953000000006, 149.05158799999998 -35.343821999999996, 149.051516 -35.343761, 149.051452 -35.34369500000001, 149.051411 -35.343641, 149.0514 -35.34361, 149.051394 -35.343554, 149.051408 -35.343514, 149.051426 -35.343478999999995, 149.051523 -35.343356, 149.05154900000002 -35.343325, 149.051579 -35.343299, 149.051614 -35.343276, 149.051652 -35.343257, 149.051824 -35.343047999999996, 149.05182 -35.343022, 149.05182299999998 -35.343002, 149.051854 -35.342940000000006, 149.051866 -35.3429, 149.051871 -35.342858, 149.051867 -35.342825, 149.051849 -35.342806, 149.051843 -35.342795, 149.051839 -35.342783000000004, 149.051835 -35.342760999999996, 149.051839 -35.34274, 149.051853 -35.342718, 149.051866 -35.342705, 149.051882 -35.342694, 149.051903 -35.342684999999996, 149.051921 -35.342681, 149.051941 -35.34268, 149.051954 -35.342681, 149.05201100000002 -35.342653000000006, 149.05205700000002 -35.342615, 149.052083 -35.342582, 149.052126 -35.342506, 149.05217 -35.342463, 149.052224 -35.342296999999995, 149.05248899999998 -35.342345, 149.05257 -35.342338, 149.05265 -35.342344, 149.052689 -35.342351, 149.052735 -35.342366999999996, 149.052805 -35.34239900000001, 149.05291100000002 -35.342403999999995, 149.053204 -35.342405, 149.053379 -35.342405, 149.05347 -35.342405, 149.05379 -35.342405, 149.054292 -35.342405, 149.05436600000002 -35.342407, 149.054458 -35.342415, 149.054569 -35.342432, 149.05469399999998 -35.342459999999996, 149.054799 -35.342492, 149.054899 -35.342532, 149.054996 -35.342578, 149.05508799999998 -35.34263, 149.055174 -35.342689, 149.055266 -35.342764, 149.055326 -35.342822999999996, 149.055371 -35.342871, 149.055632 -35.343193, 149.055708 -35.343272999999996, 149.05573700000002 -35.343301000000004, 149.05578799999998 -35.34335, 149.055872 -35.343424, 149.05594399999998 -35.34348, 149.056018 -35.343532, 149.05611299999998 -35.343596999999995, 149.05621399999998 -35.343655, 149.05631599999998 -35.343709999999994, 149.056442 -35.34377, 149.056595 -35.343831, 149.056752 -35.343882, 149.05691399999998 -35.343925, 149.057113 -35.34397, 149.057277 -35.344001, 149.05744199999998 -35.344019, 149.05740600000001 -35.344334, 149.057367 -35.344663, 149.057387 -35.344722999999995, 149.057398 -35.344786, 149.057397 -35.344840000000005, 149.05738400000004 -35.344941, 149.057422 -35.345115, 149.05745 -35.345164000000004, 149.05748200000002 -35.345202, 149.057533 -35.345251, 149.057592 -35.345292, 149.05763000000002 -35.345312, 149.057793 -35.345386, 149.059157 -35.345744, 149.059516 -35.345842, 149.05996399999998 -35.345968, 149.06040900000002 -35.346099, 149.060851 -35.346235, 149.06129099999998 -35.346375, 149.06192 -35.346583, 149.062253 -35.346687, 149.0626 -35.346796000000005, 149.06324300000003 -35.346996000000004, 149.06333500000002 -35.347025, 149.065846 -35.347815000000004, 149.06604199999998 -35.347873, 149.06632 -35.347947, 149.066601 -35.348012, 149.066845 -35.34806, 149.06713100000002 -35.348105, 149.067359 -35.348136, 149.067588 -35.34816, 149.067857 -35.348184, 149.068172 -35.348203999999996, 149.068487 -35.348213, 149.068756 -35.348214, 149.06880900000002 -35.348213, 149.069023 -35.348198, 149.069499 -35.34816, 149.069593 -35.348153, 149.06987 -35.348127000000005, 149.07026499999998 -35.348086, 149.070637 -35.348042, 149.071152 -35.347978000000005, 149.073482 -35.347691, 149.073891 -35.347643000000005, 149.074351 -35.347590000000004, 149.074738 -35.347546, 149.075213 -35.347485, 149.07550700000002 -35.347455, 149.075853 -35.347428, 149.076249 -35.347411, 149.076594 -35.347407000000004, 149.076942 -35.347413, 149.07728799999998 -35.347429, 149.07775700000002 -35.347462, 149.07814 -35.347502, 149.078521 -35.347553999999995, 149.07880600000001 -35.347601, 149.07908799999998 -35.347656, 149.0819 -35.348245, 149.082477 -35.348377, 149.083051 -35.348517, 149.083259 -35.348561, 149.083426 -35.348595, 149.083722 -35.348645, 149.084021 -35.348687, 149.084226 -35.348709, 149.084742 -35.348746000000006, 149.085831 -35.348778, 149.08624 -35.34879, 149.086299 -35.348791999999996, 149.086714 -35.348805, 149.087824 -35.348839, 149.088317 -35.348853999999996, 149.089159 -35.348865999999994, 149.089527 -35.348773, 149.089566 -35.348757, 149.08961100000002 -35.348727000000004, 149.089641 -35.348693, 149.089659 -35.348653999999996, 149.089668 -35.348606, 149.089482 -35.348209999999995, 149.08944800000003 -35.348151, 149.089268 -35.347827, 149.08908799999998 -35.347528999999994, 149.089045 -35.347463, 149.08893999999998 -35.347298, 149.088856 -35.347174, 149.088758 -35.346999, 149.08868600000002 -35.346843, 149.088615 -35.34666, 149.088579 -35.346543, 149.08854399999998 -35.346402000000005, 149.08842 -35.345779, 149.08832200000003 -35.345287, 149.08821899999998 -35.344839, 149.087982 -35.344877000000004, 149.087696 -35.344922, 149.086995 -35.345034999999996, 149.086966 -35.345043, 149.08694 -35.345055, 149.086919 -35.345071000000004, 149.086904 -35.345085, 149.086817 -35.345087, 149.086569 -35.345121999999996, 149.086549 -35.345121, 149.086517 -35.345117, 149.08648300000002 -35.345107, 149.08645 -35.345089, 149.086425 -35.345065999999996, 149.08641200000002 -35.345048, 149.086399 -35.345023, 149.086352 -35.344822, 149.086356 -35.344796, 149.086376 -35.344747999999996, 149.08639 -35.344726, 149.086415 -35.344703, 149.08646299999998 -35.344671000000005, 149.08649 -35.344659, 149.086527 -35.344648, 149.087278 -35.344541))"

#route: 19
def remove_extras(coords : str):
    '''
    Removes the MULTILINESTRING ((...)) part and separates each entry by commas
    '''
    coords = coords.replace("MULTILINESTRING ((","").replace("))", "")
    coordinates_str = coords
    # split into multiple pairs
    coordinates_list = coordinates_str.split(", ")
    return coordinates_list

#convert the first values into float
def convert_to_int(coordinates_list : list):
    '''
    Converts list to float for getting accurate coordinates
    '''
    AX, AY = map(float, coordinates_list[0].split())
    AX = int(AX)
    AY = int(AY)

    return AX, AY

def get_raw_coordinates(coordinates_list : list):
    '''
    converts coordinates from API to a lsit (does not make it usuable for drawing the map)
    '''
    raw_coordinates = []
    for pair in coordinates_list:
        x, y = pair.split(" ")
        raw_coordinates.append((x, y))
    
    return raw_coordinates

def set_screen():
    '''
    Create main screen 
    '''
    wl = -1000
    wb = -1000
    wr = 1000
    wt = 1000
    turtle.Screen().setworldcoordinates(wl, wb, wr, wt)

def get_coordinates(raw_coordinates : list, coordinates_list: list, multiplier:int):
    '''
    Converts raw coordinates to usuable coordinates by removing the whole number value from the float and using a multiplier
    '''
    coordinates = []
    trun_x = trun(coordinates_list)[0]
    trun_y = trun(coordinates_list)[1]
    MULTIPLIER = multiplier*1000
    X0 = ((float(raw_coordinates[0][0]) - trun_x) *MULTIPLIER)
    Y0 = (((float(raw_coordinates[0][1])+ abs(trun_y))*MULTIPLIER))
    

    for i in range(len(raw_coordinates)):
        x = ((float(raw_coordinates[i][0]) - trun_x) *MULTIPLIER) - X0
        y = (((float(raw_coordinates[i][1])+ abs(trun_y))*MULTIPLIER)) - Y0

        coordinates.append((float(x), float(y)))
    return coordinates

def draw_route(coordinates , colour, size):
    '''
    Draws the route using the coordinates from get_coordinate function
    '''
    turtle.color(colour)
    turtle.pensize(size)
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(0,0)
    turtlepos = []
    for i in range(0, len(coordinates)):
        turtle.goto(coordinates[i])
        turtle.pendown()
        turtlepos.append(turtle.position())
        turtle.hideturtle()

    return turtlepos

def rescale_image(map_pos: list, border : int):
    '''
    Scales the map to fit the screen in case it goes off screen or is too big
    '''
    wl = min(map_pos, key=lambda x: x[0])
    wr = max(map_pos, key=lambda x: x[0])
    wb = min(map_pos, key=lambda x: x[1])
    wt = max(map_pos, key=lambda x: x[1])

    WHITESPACE = border
    turtle.Screen().setworldcoordinates(wl[0]-WHITESPACE, wb[1]-WHITESPACE, wr[0]+WHITESPACE, wt[1]+WHITESPACE)

def trun(coordinates_list : list):
    '''
    Separates the int value from the floats
    '''
    trun_x = float(convert_to_int(coordinates_list)[0])
    trun_y = float(convert_to_int(coordinates_list)[1])

    return list((trun_x, trun_y))

def main(coords, colour, size, border, multiplier):
    '''
    Uses functions to draw the map,
    coords = coordinates can use API to get them,
    colour = map line color,
    size = pen size for map drawing,
    border = border around the map to keep away from corners of the screen,
    multiplier = the size map is drawn at
    '''
    set_screen()
    # split each pair into x and y components
    coordinates_list = remove_extras(coords)
    raw_coordinates = list(get_raw_coordinates(coordinates_list))
    coordinates = list(get_coordinates(raw_coordinates, coordinates_list, multiplier))
    map_pos = draw_route(coordinates, colour, size)
    rescale_image(map_pos, border)
    turtle.mainloop()