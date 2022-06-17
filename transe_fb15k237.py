from pykeen.pipeline import pipeline
from pykeen.datasets import FB15k237
import torch
from pykeen.evaluation import RankBasedEvaluator

model = torch.load('S:\\model_fb15k237_TransE\\trained_model.pkl', map_location=torch.device('cpu'))
dataset = FB15k237()
evaluator = RankBasedEvaluator(filtered=True,)
mapped_triples = dataset.testing.mapped_triples
results = evaluator.evaluate(
    model=model,
    mapped_triples=dataset.testing.mapped_triples,
    additional_filter_triples=[
        dataset.training.mapped_triples,
        dataset.validation.mapped_triples,
    ],
)
print('TransE Fb15k-237 evaluation:')
print('hits_at_10')
print(results.get_metric('hits_at_10'))
print('hits_at_5')
print(results.get_metric('hits_at_5'))
print('hits_at_3')
print(results.get_metric('hits_at_3'))

