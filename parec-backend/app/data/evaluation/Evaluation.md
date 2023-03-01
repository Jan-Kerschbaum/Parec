## 📊 Evaluation of Parec
***

1. 👾 [Comparison Against Random Baseline](#comparison_against_random_baseline)
2. 🧐 [Subjective Qualitative Evaluation](#subjective_qualitative_evaluation)

***

### 👾 Comparison Against Random Baseline <a name="comparison_against_random_baseline"></a>

The following table will compare three chosen abstracts by a [random baseline](baselines.py) and the top three as recommended by our application Parec, based on the query `engineering`. You can find the abstracts if you click on the provided links.

|**Query: `enginieering`**|**Random Baseline**|**Parec**|
|-----|----------|-----------|
|**Article**| [SurReal: enhancing Surgical simulation Realism using style transfer](https://arxiv.org/abs/1811.02946) | [Towards Digital Engineering -- The Advent of Digital Systems Engineering](https://arxiv.org/abs/2002.11672) |
|**arxiv category**|Computer Science > Computer Vision and Pattern Recognition|Computer Science > Computers and Society|
|**Relevance**|None|High|
|**Article**| [Fast Gravitational Approach for Rigid Point Set Registration with Ordinary Differential Equations](https://arxiv.org/abs/2009.14005) | [Advancing Behavior Engineering: Toward Integrated Events Modeling](https://arxiv.org/abs/2101.01325) |
|**arxiv category**|Computer Science > Computer Vision and Pattern Recognition|Computer Science > Software Engineering|
|**Relevance**|None|High|
|**Article**| [Edge-Based Collision Avoidance for Vehicles and Vulnerable Users: An Architecture Based on MEC](https://arxiv.org/abs/1911.05299) | [Software Engineering Meets Systems Engineering: Conceptual Modeling Applied to Engineering Operations](https://arxiv.org/abs/2110.13995) |
|**arxiv category**|Computer Science > Networking and Internet Architecture|Computer Science > Software Engineering|
|**Relevance**|None| High|
|**Related terms**|['models.' 'optimal' 'deploy' 'quantization' 'focus).' 'is' 'class' 'function' 'resulting' 'discussed' 'obtained' 'system' 'vehicle,' 'education.' 'quasilinear' 'ratio' 'architecture' 'if' 'non-deep-learning-based' 'force'] | ['tm', 'thinging', 'conceptual', 'modeling', 'tm modeling', 'conceptual modeling', 'diagrams', 'diagram', 'machine tm', 'conceptual model', 'conceptual framework', 'notions', 'called thinging', 'thinging machine', 'description', 'notion', 'modeling language', 'modeling methodology', 'ontology', 'language modeling']|
|**Relevance**|Limited|Medium|

ℹ️ Note that not all terms proposed by Top2Vec seem to have a high relevance for the query and the list contains many terms not found in the abstracts. While the recommended papers seem to be of the relevant topic, there could be some limitations to Top2Vec in regard to the most similar terms found for a query.

💡 Conclusion: Our system consistently and substantially outperforms the random baseline.

***
### 🧐 Subjective Qualitative Evaluation <a name="subjective_qualitative_evaluation"></a>

We have no Gold Standard for our results, but in order to evaluate the quality subjectively, we performed a blind experiment among our team members. For this, one team member entered five different search queries in our application, and sent the top three recommended abstract links to another team member. This team member then went through the abstracts and noted the most relevant terms for each. For each evaluated query, we put the found terms in a list, and investigated if these terms were present in the generated graph of our system. The results are compared below:

|**Query**|**Related terms chosen by team member (considered as Gold Standard)**|**Terms present in the generated topic graph**|
|-------------|-------------|-----------------|
|**`ai`**| Artificial Intelligence (x2), Deep Learning, Edge Computing (x2), Machine Learning, Artificial Neural Networks, Topology, COVID-19, Blockchain, Internet of Medical Things| ⚡️ Query was not found, but Artificial Intelligence was found twice (AI is its acronym); 🌐 Terms present in graph: Artificial Intelligence (x2), Edge Intelligence (synonym to Edge Computing (x2))|
|**`transfer learning`**| Dynamic Distribution Adaption, Transfer Learning (x3), Machine Learning (x2), Deep Learning, Regularization, Bottleneck Feature Extraction, Deep Neural Networks, COVID-19 | 💡 Query was found thrice: Transfer Learning (x3) |
|**`engineering`**|Software Engineering (x3), System Development Process, Requirements Engineering, Computer Games Development, Software Testing, Soft Skills| ⚡️ Query was not found, but data-domain-specific subterm: Software Engineering (x3); 🌐 Terms present in graph: Requirements Engineering, Software Testing|
|**`computer vision`**|Machine Learning, Artificial Intelligence, Visual Question Answering, Neural Networks, Natural Language Processing (x3), Multimodal Content Retrieval, Computer Vision, Turkish Language| 💡 Query was found once: Computer Vision; 🌐 Terms present in graph:  Natural Language (synonym to Natural Language Processing)|
|**`natural language processing`**|Natural Language Processing (x2), Discourse Parsing, Artificial Intelligence, Analyzing News Headlines, Syntactic Parsing, IT Security, Parsing| 💡 Query was found twice: Natural Language Processing (x2); 🌐 Terms present in graph: Syntactic Parsing, Parsing |


ℹ️ Note that in all graphs, more Gold labels extracted from the three papers were not found - with the exception of the `engineering` query, where the amounts were equal. At the same time, the actual query term was often an extracted Gold Standard label or its synonym, sourced from several of the papers' abstracts by the team member.

💡 As a conclusion, we can infer that (1) the papers are relevant to the query, which was the primary objective, but (2) the recommended papers may not represent the broader topic, and (3) the Top2Vec model emphasizes different features than an average human reader.