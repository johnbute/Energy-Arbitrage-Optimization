# Decision-focused learning for battery control

Honours project: schedule a battery for a 1 MW data centre under uncertain electricity prices,
first by predicting prices and then optimising (learn-then-optimise), then by training the price
model on the cost of the decisions it leads to (decision-focused learning).

## Layout

```
docs/                      reference paper (decision_focused_learning_for_battery_control.pdf)
task_1/                    warm-up: a small convex optimisation in cvxpy
task_1.5/                  battery LP with known prices and demand
  data/price_data/           day-ahead LMP files
  data/demand_data/          data-centre power profiles (separate git repo)
  scripts/script.ipynb       the LP and the cost-vs-capacity sweep
  report/                    LaTeX write-up
  visualizations/
task_2/                    learn-then-optimise, and Task 3 (decision-focused learning)
  data/storage_data.csv      hourly prices, load forecast and temperature, 2011-2016
  inspo/                     reference code (Donti et al.) the price network is based on
  script/task_2.ipynb        all of Tasks 2 and 3, see below
  report/                    (empty)
  visualizations/            figures saved by the notebook
requirements.txt
```

`task_2/script/task_2.ipynb` sections:

| Section | What it does |
|---|---|
| 2.1 | price network trained on MSE, residual variance, calibration |
| 2.2 | battery LP at predicted prices, regret against hindsight, capacity sweep |
| 4.1 | where the regret comes from (worst days, accuracy vs decision quality) |
| 3.1 | differentiable battery layer (cvxpylayers), gradient checks, choice of eps |
| 3.2 | decision-focused training, comparison with the MSE model, capacity and eps sweeps |

## Running

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Open the notebooks from their own folder: they find the data with `Path.cwd().parent`.
`task_2.ipynb` also reads the demand profiles from `task_1.5/data/demand_data/`, so keep the two
task folders side by side.
