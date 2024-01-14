import random

easy_sentences = [
    "The sun shines brightly in the blue sky, casting a warm glow over the green fields.",
    "Children play joyfully in the park, laughing and running around without a care in the world.",
    "A cozy blanket and a good book make for a perfect evening by the fireplace.",
    "Birds chirp happily in the trees, creating a melodic soundtrack to a peaceful afternoon.",
    "The smell of freshly baked cookies wafts through the kitchen, enticing everyone in the house.",
    "A friendly dog greets you at the door, wagging its tail with excitement.",
    "Flowers bloom in vibrant colors, adding beauty to the garden in the spring.",
    "A gentle breeze rustles the leaves, providing a refreshing break from the summer heat.",
    "The smell of rain lingers in the air as thunder rumbles in the distance.",
    "Warm sand between your toes and the sound of waves create a relaxing atmosphere at the beach.",
    "A rainbow appears after the rain, painting the sky with a spectrum of colors.",
    "A simple picnic with sandwiches and fruit is a delightful way to spend a sunny day.",
    "The cozy cabin by the lake offers a peaceful retreat from the hustle and bustle of city life.",
    "A smiling face and a kind word can brighten anyone's day.",
    "Stargazing on a clear night reveals the beauty of the universe, with countless stars twinkling overhead."
]

medium_sentences = [
    "Under the twinkling stars, a campfire crackled, casting flickering shadows on the faces of friends sharing tales of adventure and dreams.",
    "A vintage typewriter sat on the dusty desk, its keys telling stories of bygone eras with each nostalgic click.",
    "Deep in the enchanted forest, mystical creatures whispered secrets to the moonlit trees, creating an otherworldly symphony of nature's magic.",
    "The old lighthouse stood tall against the crashing waves, guiding ships to safety with its timeless beam of light.",
    "At the top of the mountain, a lone eagle soared through the crisp air, surveying the vast landscape below with keen eyes.",
    "In the quiet library, the scent of aged books mingled with the soft murmur of turning pages, creating a sanctuary for avid readers.",
    "Beneath the cherry blossom tree, a gentle breeze carried petals through the air, painting a delicate picture of fleeting beauty.",
    "Along the cobblestone streets, a street performer played a melancholic tune on a weathered violin, captivating the passing crowd.",
    "As night fell, a bonfire illuminated the beach, casting a warm glow on the faces of friends enjoying the simple pleasure of togetherness.",
    "In the attic, forgotten trinkets and dusty memories lay hidden in old boxes, waiting to be rediscovered by curious hands.",
    "Through the open window, the scent of rain mingled with the sound of distant thunder, creating a soothing symphony of a coming storm.",
    "At the edge of the meadow, a lone deer grazed peacefully, its elegant silhouette blending seamlessly with the golden hues of sunset.",
    "A cozy cabin nestled in the snowy mountains welcomed weary travelers with the inviting warmth of a crackling fireplace and mugs of hot cocoa.",
    "In the heart of the bustling city, neon lights reflected off rain-slicked streets, creating a vibrant and dynamic tableau of urban life.",
    "Among the ancient ruins, the echoes of history whispered tales of empires risen and fallen, leaving behind the enigmatic traces of the past."
]

hard_sentences = [
    "The perplexing conundrum, rife with intricacies, confounds even the most adept investigators, demanding a comprehensive analysis of the cryptic clues scattered throughout the enigmatic scene.",
    "In the labyrinthine corridors of academia, erudite scholars engage in profound discourse, probing the existential implications of esoteric philosophies, leaving audiences in contemplative silence.",
    "The polymathic researcher delves into the multifaceted realms of theoretical physics, navigating the complex tapestry of quantum entanglement, wave-particle duality, and stochastic processes.",
    "Amidst the cacophony of the metropolis, audacious avant-garde artists challenge societal norms, deconstructing traditional paradigms through surrealist expressions that defy conventional aesthetic conventions.",
    "The labyrinthine legal document, fraught with convoluted legalese and nuanced stipulations, perplexes even seasoned jurists, necessitating a meticulous examination of its intricate clauses and provisions.",
    "The astute neuroscientist embarks on a meticulous exploration of synaptic connections, unraveling the enigmatic mechanisms governing neural plasticity, cognitive processes, and the intricacies of memory formation.",
    "In the digital frontier, technological pioneers develop algorithms that discern intricate patterns within vast datasets, revolutionizing machine learning and artificial intelligence paradigms across diverse industries.",
    "The erudite orator, with eloquence and panache, expounds upon abstruse philosophical tenets, traversing the intricate landscape of existential quandaries that permeate the human psyche and collective consciousness.",
    "The avant-garde architect conceptualizes structures that transcend conventional paradigms, blending postmodernist influences with neofuturistic designs, challenging perceptions of spatial dynamics and urban aesthetics.",
    "The intrepid explorer, navigating the treacherous terrains of uncharted wilderness, uncovers artifacts that encapsulate the vestiges of ancient civilizations, shedding light on the enigmatic mysteries of bygone eras.",
    "The computational linguist deciphers cryptic scripts, unraveling linguistic codes embedded in ancient texts, shedding light on the syntactical nuances and semantic intricacies of historical languages.",
    "The seasoned diplomat negotiates delicate geopolitical alliances, navigating the nuanced landscape of international relations, confronting the myriad challenges that arise from intricate political entanglements.",
    "In the theoretical realm of abstract mathematics, the prodigious mathematician formulates elegant proofs that traverse the intricate lattice of axioms, theorems, and geometric conjectures, unraveling the profound beauty of numerical abstraction.",
    "The oratorical maestro, with a symphony of words, traverses the cadence of rhetorical nuances, commanding the attention of the audience with a masterful blend of persuasive discourse and linguistic finesse.",
    "Amidst the tumultuous currents of global economic shifts, the savvy entrepreneur navigates the intricate landscape of market dynamics, capitalizing on strategic opportunities to redefine industry paradigms and spur innovation."
]


def easy_paragraph():
    return random.choice(easy_sentences)

def medium_paragraph():
    return random.choice(medium_sentences)

def hard_paragraph():
    return random.choice(hard_sentences)