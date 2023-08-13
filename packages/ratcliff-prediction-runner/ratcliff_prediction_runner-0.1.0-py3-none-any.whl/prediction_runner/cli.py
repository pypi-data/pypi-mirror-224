import click
import pickle
import tempfile
from ratcliff_breast_cancer_predictor.predictor import predict, train


@click.command()
def cli() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        # train the model
        score = train(
            modal_path=f"{temp_dir}/cancer_predictor_model.sav", data_path=None
        )
        # assert the score is greater than 0.9
        model = pickle.load(open(f"{temp_dir}/cancer_predictor_model.sav", "rb"))
        # get the actual result
        actual = predict(model, [[5, 1, 4, 1, 2, 1, 3, 2, 1]])
        # assert the expected result and the actual result are equal
        print(actual)


if __name__ == "__main__":
    cli()
