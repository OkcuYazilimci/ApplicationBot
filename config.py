# General bot settings

# browser you want the bot to run ex: ["Firefox"], ["Chrome"] choose one only
browser = ["Firefox"]
# Optional! run browser in headless mode, no browser screen will be shown it will work in background.
headless = True
# Optional! for Firefox enter profile dir to run the bot without logging in your account each time
firefoxProfileRootDir = r""
# If you left above field empty enter your Linkedin password and username below
# Linkedin credits
email = ""
password = ""

# These settings are for running Linkedin job apply bot
LinkedinBotProPasswrod = ""
# location you want to search the jobs - ex : ["Poland", "Singapore", "New York City Metropolitan Area", "Monroe County"]
# continent locations:["Europe", "Asia", "Australia", "NorthAmerica", "SouthAmerica", "Africa", "Australia"]
location = ["Turkey", "Europe", "Asia", "Australia", "NorthAmerica", "SouthAmerica", "Africa", "Australia", "Germany", "United States", "WorldWide"]
# keywords related with your job search
keywords = ["Backend", "Specialist", "developer", "junior", "associate", "node.js", "java", "python", "Software Engineer", "Software Developer", "Backend Developer", "Fullstack Developer", "Java Developer"]
# keywords = ["programming"]
#job experience Level - ex:  ["Internship", "Entry level" , "Associate" , "Mid-Senior level" , "Director" , "Executive"]
experienceLevels = ["Associate", "Entry Level", "Mid Level"]
#job posted date - ex: ["Any Time", "Past Month" , "Past Week" , "Past 24 hours"] - select only one
datePosted = ["Any Time"]
# datePosted = ["Past 24 hours"]
#job type - ex:  ["Full-time", "Part-time" , "Contract" , "Temporary", "Volunteer", "Intership", "Other"]
jobType = ["Full-time", "Part-time" , "Internship"]
#remote  - ex: ["On-site" , "Remote" , "Hybrid"]
remote = ["On-site" , "Remote" , "Hybrid"]
#salary - ex:["$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+" ] - select only one
salary = [""]
#sort - ex:["Recent"] or ["Relevent"] - select only one
sort = ["Recent"]
#Blacklist companies you dont want to apply - ex: ["Apple","Google"]
blacklist = [""]
#Blaclist keywords in title - ex:["manager", ".Net"]
blackListTitles = [""]
#Only Apply these companies -  ex: ["Apple","Google"] -  leave empty for all companies 
onlyApply = [""]
#Only Apply titles having these keywords -  ex:["web", "remote"] - leave empty for all companies 
onlyApplyTitles = [""] 
#Follow companies after sucessfull application True - yes, False - no
followCompanies = True
# your country code for the phone number - ex: fr
country_code = ""
# Your phone number without identifier - ex: 123456789
phone_number = ""


# These settings are for running AngelCO job apply bot
AngelCoBotPassword = ""
# AngelCO credits
AngelCoEmail = ""
AngelCoPassword = ""
# jobTitle ex: ["Frontend Engineer", "Marketing"]
angelCoJobTitle = ["Backend Engineer", "Software Engineer", "Java Developer", "Junior"]
# location ex: ["Poland"]
angelCoLocation = ["Poland", "Germany", "Europe", "United States", "United Kingdom", "Turkey", "Australia"]

# These settings are for running GlobalLogic job apply bot
GlobalLogicBotPassword = ""
# AngelCO credits
GlobalLogicEmail = ""
GlobalLogicPassword = ""
# Functions ex: ["Administration", "Business Development", "Business Solutions", "Content Engineering", 	
# Delivery Enablement", Engineering, Finance, IT Infrastructure, Legal, Marketing, People Development,
# Process Management, Product Support, Quality Assurance,Sales, Sales Enablement,Technology, Usability and Design]
GlobalLogicFunctions = ["Engineering"]
# Global logic experience: ["0-1 years", "1-3 years", "3-5 years", "5-10 years", "10-15 years","15+ years"]
GlobalLogicExperience = ["0-1 years", "1-3 years"]
# Global logic location filter: ["Argentina", "Chile", "Crotia", "Germany", "India","Japan", "Poland"
# Romania, Sweden, Switzerland,Ukraine, United States]
GlobalLogicLocation = ["poland"]
# Freelance yes or no
GlobalLogicFreelance = ["no"]
# Remote work yes or no
GlobalLogicRemoteWork = ["yes"]
# Optional! Keyword:["javascript", "react", "angular", ""]
GlobalLogicKeyword = ["react"]
# Global Logic Job apply settinngs
FirstName = ""
LastName = ""
Email = ""
LinkedInProfileURL = "www.google.com"
Phone = "" #OPTIONAL
Location = "" #OPTIONAL
HowDidYouHeard = "" #OPTIONAL
ConsiderMeForFutureOffers = True #true = yes, false = no