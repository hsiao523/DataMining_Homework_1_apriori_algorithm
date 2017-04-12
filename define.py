#變數定義檔

WORK_PATH="E:\\Google 雲端硬碟\碩士在職專班\\105學年度\第二學期\\Data Mining\\Homework\\Homework1\\test_Data\\"

TRANS_DATA_1={'sup':5,"input_file":r"T15I7N0.5KD1K.txt"}
TRANS_DATA_2={'sup':50,"input_file":r"T15I7N0.5KD10K.txt"}
TRANS_DATA_3={'sup':500,"input_file":r"T15I7N0.5KD100K.txt"}
TRANS_DATA_4={'sup':30000,"input_file":r"T15I7N0.5KD1000K.txt"}
TRANS_DATA_5={'sup':1000,"input_file":r"T15I7N0.5KD1000K.txt"}

BIN_TRANS_DATA_1={'sup':5,"input_file":r"T15I7N0.5KD1K.data"}
BIN_TRANS_DATA_2={'sup':50,"input_file":r"T15I7N0.5KD10K.data"}
BIN_TRANS_DATA_3={'sup':500,"input_file":r"T15I7N0.5KD100K.data"}
BIN_TRANS_DATA_4={'sup':30000,"input_file":r"T15I7N0.5KD1000K.data"}
BIN_TRANS_DATA_5={'sup':1000,"input_file":r"T15I7N0.5KD1000K.data"}


CURRENT_TRANS_DATA=BIN_TRANS_DATA_3

INPUT_FILE=CURRENT_TRANS_DATA['input_file']
MIN_SUP=CURRENT_TRANS_DATA['sup']

BUFFER_SIZE=4000000

#SUB_NODE_SET=1
#ITEM_SET=2
#COUNT=3
