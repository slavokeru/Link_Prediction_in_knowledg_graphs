from pykeen.pipeline import pipeline
from pykeen.datasets import Nations
pipeline_result = pipeline(
    dataset='Nations',
    model='ComplEx',
    epochs=20
)
pipeline_result.save_to_directory('S:\\model_Nations_Complex')
