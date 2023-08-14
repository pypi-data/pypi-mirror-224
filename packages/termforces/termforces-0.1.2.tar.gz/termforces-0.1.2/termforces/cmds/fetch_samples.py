import click
from termforces.termforces_shell import termforces_shell, State
import os


@termforces_shell.command(name='download-samples')
@click.argument('problem_index')
@click.argument('samples_dir')
@click.option('--contest-id')
@click.pass_obj
def download_samples(state: State, contest_id, problem_index, samples_dir):
    if contest_id is None:
        if state.contest_id is not None:
            contest_id = state.contest_id
        else:
            print('Specify contest id or enter contest via enter-contest command')
            return
    if not os.path.isdir(samples_dir):
        print('No such directory')
    samples = state.scraper.get_samples(contest_id, problem_index)
    for i, sample in enumerate(samples):
        with open(os.path.join(samples_dir, f'{i+1:03d}'), 'w') as f:
            f.write(sample.s_in)
        with open(os.path.join(samples_dir, f'{i+1:03d}.a'), 'w') as f:
            f.write(sample.s_out)
