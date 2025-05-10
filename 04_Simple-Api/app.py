from fastapi import FastAPI
import random

# We wil build three simple get endpoints.
# 01_ Side_Hustles
# 02_ Money_Quotes
# 03_ funny_jokes

app = FastAPI()

side_hustle = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. - Dave Ramsey",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don't stay in bed unless you can make money in bed. - George Burns",
    "Money often costs too much. - Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. - Warren Buffett",
    "It's not about having lots of money. It's about knowing how to manage it. - Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Zig Ziglar",
    "Being rich is having money; being wealthy is having time. - Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. - Jonathan Swift",
    "Money grows on the tree of persistence. - Japanese Proverb",
]


funny_jokes = [
    "Teacher: Agar zameen se sona nikle toh kya kehlata hai? Student: Surprise test! 😆📚",
    "Teacher: Tum exam mein itne blank kyun ho? Student: Sir, silence is the best answer! 🤫📝",
    "Doctor: Aap roz exercise karte ho? Patient: Haan, sochta zarur hoon! 🧠🏋️",
    "Boy: Tumhara naam kya hai? Girl: Google. Boy: Kyun? Girl: Tumhara har sawaal ka jawab hai mere paas! 🔍💁‍♀️",
    "Friend 1: Yaar mobile gir gaya tha. Friend 2: Tut gaya? Friend 1: Nahi, uthaya aur maafi mang li! 📱🙏",
    "Mom: Kitni baar bola hai, TV kam dekho! Beta: OK, volume kam kar deta hoon! 📺🔉",
    "Teacher: Tumhe sharam nahi aati? Student: Aati hai sir, par late hoti hai! 😅⌛",
    "Boss: Tum late kyun aaye? Employee: Sir, sapna adhoora reh gaya tha! 🛌⏰",
    "Wife: Suno ji, ek baat kahun? Husband: Pehle kaunsi suna hai? 😒💬",
    "Boy: Tum mujhe ignore kar rahi ho? Girl: Nahi, training de rahi hoon future ke liye! 🚫🎓",
    "Friend: Mere paas bike hai, car hai, bungla hai. Tumhare paas kya hai? Me: Mere paas neend hai bhai! 😴💤",
    "Girl: Mujhe shopping pasand hai. Boy: Mujhe bachat pasand hai. Toot gaya rishta! 🛍️💔",
    "Student: Paper mushkil tha. Teacher: Kyun? Student: Kyunki padhai nahi ki thi! 📚🤯",
    "Friend: Tumhara WhatsApp status badal gaya? Me: Haan, mood swing tha! 📱😵",
    "Boy: Tum smile bahut achi karti ho. Girl: Free ka hai, tu bhi karle! 😊😜",
    "Girl: Main tumse naraz hoon. Boy: Achha? Phir toh party banti hai! 🎉🙃",
    "Boy: Tum ro kyun rahi ho? Girl: Data khatam ho gaya! 😭📶",
    "Doctor: Aapko kya takleef hai? Patient: Mobile charge nahi hota! 🔋😩",
    "Teacher: Itne late kyun aaye? Student: Neend se rishta purana hai sir! 🛏️😌",
    "Friend 1: Exam ready hai? Friend 2: Haan, tayyari duaon tak pohanch gayi hai! 🙏📝",
    "Boy: Main tumhare bina nahi reh sakta! Girl: Toh oxygen cylinder le lo! 🥲🧴"
]


# Side Hustle api
# decorator
@app.get("/side_hustle")
def get_side_hustles():
    """Return a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustle)}

# Money Quotes api
@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quotes"""
    return{"money_quotes":random.choice(money_quotes)}


# API WITH KEY 
# @app.get("/money_quotes")
# def get_money_quotes(apikey:str):
#     """Return a random money quotes"""
#     if apikey != "1234":
#         return {"Error":"Invalid api key"}
#     return{"money_quotes":random.choice(money_quotes)}



@app.get("/funny_jokes")
def get_funny_jokes():
    """Return a Random Jokes"""
    return{"Funny_jokes":random.choice(funny_jokes)}