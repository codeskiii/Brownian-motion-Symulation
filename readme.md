# Brownian motion symulation
## Instaling

* 1. install dependencies

```
pip install -r requirements.txt
```
* 2. run run.py

```
python run.py
```

## Config file

* Variables

| Variable      |   Explanation    |
| ------------- | ---------------- |
| scale         | 10 ** x          |
| temp_in_k     | temperature in k |
|ressistance_coeficient | ressistance coeficient |
| particle_mass | particle mass |
| num_of_particles | number of particles|

* Example

```
{
    "scale":12,
    "temp_in_k":300,
    "ressistance_coeficient":"1e-9",
    "particle_mass":"1e-21",
    "num_of_particles":100
}
```