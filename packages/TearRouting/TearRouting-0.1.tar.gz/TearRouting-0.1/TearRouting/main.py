import openai, time, os
from router.inner import Router

class Tear:
    def __init__(self, api_key, organization = False):
        openai.api_key = api_key
        if organization: openai.organization = org
        self.internalRouter = Router()
        self.buckets = self.internalRouter.buckets
    
    def addBuckets(self, buckets): # Add training categories.
        code = self.internalRouter.addBuckets(buckets)
        return code

    def removeBuckets(self, buckets): # Remove training categories.
        code = self.internalRouter.removeBuckets(buckets)
        return code
    
    def train(self, questions, batchSize=5): # Train the model from a list of questions.
        code = self.internalRouter.trainWithFile(questions, batchSize)
        return {"code" : code[0], "cost" : code[1]}

    def manualRoute(self, inp): # Route the question with LLM instead of embeddings without adding to training data.
        code = self.internalRouter.manualAnswer(inp)
        return {"output" : code[0], "code" : code[1]}

    def route(self, inp): # Route the question using embeddings.
        code = self.internalRouter.route(inp)
        return {"output" : code[0], "code" : code[1]}

    def routeLearn(self, inp): # Train the model while also routing questions.
        code = self.internalRouter.learnAndRoute(inp)
        return {"output" : code[0], "code" : code[1]}

    def wipe(self): # Wipe the training data.
        code = self.internalRouter.wipe()
        return code


questions = [
    "What genre is The Godfather?",
    "Does Forrest Gump have a plot about war?",
    "Who stars in Titanic?",
    "Is The Shawshank Redemption a good movie?",
    "When was Pulp Fiction released?",
    "Is The Matrix an action movie?",
    "What's the plot of Inception?",
    "Did critics like La La Land?",
    "Who directed Parasite?",
    "Is Toy Story animated?",
    "What genre is Home Alone?",
    "Does Frozen have singing?",
    "Who plays Neo in The Matrix?",
    "Is Citizen Kane a highly rated movie?",
    "When did Avatar come out?",
    "Is The Hangover a comedy?",
]
buckets = {
    "Genre" : "Questions about the genre or genres of a movie (e.g. Is it a comedy? Is it a romantic comedy?",
    "Plot" : "Questions about the storyline or events in a movie (e.g. What happens in the movie? Who is the main character?)",
    "Cast_Characters" : "Questions about the actors or characters in a movie (e.g. Who stars in it? Who plays the main character?)",
    "Reviews Opinions" : "Questions asking for subjective thoughts or critiques of a movie (e.g. Is it any good? What do critics say about it?)",
    "Details" : "Factual questions about specific details of a movie (e.g. When was it released? Who directed it? Where was it filmed?)"
}

router = Tear("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")
router.addBuckets(buckets)
router.wipe()
router.train(questions, 20)
while True:
    query = input("~ ")
    print("\n" + router.route(query)["output"] + "\n")