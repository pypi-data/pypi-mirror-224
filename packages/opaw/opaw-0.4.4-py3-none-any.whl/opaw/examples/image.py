from opaw.util import log
from opaw.model.image import ImageBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# logger
logger = log.get("image", "logs/image.log")

# image
bot = ImageBot()

# create a image (URL)
prompt = "A black cat sitting on a frozen lake."
response = bot.create(prompt, task="create", size="256x256")
url = response['data'][0]['url']
bot.save_img(url, "imgs/img-url.jpg")
logger.info(f"image: {url}")

# data scheme (URI) (base64)
response = bot.create(prompt, task="create", size="256x256", response_format="b64_json")
uri = response['data'][0]['b64_json']
bot.save_img(uri, "imgs/img-uri.jpg")
# logger.info(f"image: {uri}")  # too long to print

# save history if needed
bot.save_history("history/image-hist.json")
