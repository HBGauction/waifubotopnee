import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = "1381668733"
sudo_users = ["1381668733", "6004043453"]
GROUP_ID = "-1002369035531"
TOKEN = "7567555779:AAFA7hx8Q-orYico0ojGrp6V80pRFXiFl6g"
mongo_url = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/a17bbdf36197b0f0eb2c1.jpg", "https://telegra.ph/file/4754711cd88be32baf5b4.jpg", "https://telegra.ph/file/46b1151c6088fabc62250.jpg", "https://telegra.ph/file/4ed692d4e678216f87083.jpg"]
SUPPORT_CHAT = "Anime_Asia_Community"
UPDATE_CHAT = "Anime_Asia_Community"
BOT_USERNAME = "Son_Goku_ro_bot"
CHARA_CHANNEL_ID = "-1002369035531"
api_id = "23734455"
api_hash = "40972650709e0e2b0aa58734f3524261"

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
