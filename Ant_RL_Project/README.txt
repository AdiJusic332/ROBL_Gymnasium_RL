ANT-Simulation

# 1. Voraussetzungen

- Windows 10/11
- Python 3.12
- Grafiktreiber mit starker Leistung
- Visual Studio Code (empfohlen)

Python 3.12 herunterladen: https://www.python.org/downloads/

# 2. Projektordner erstellen

[PowerShell öffnen -> Befehle eingeben]
mkdir Ant_RL_Project
cd Ant_RL_Project


## 3. Virtuelle Umgebung erstellen

[Powershell]
py -3.12 -m venv .venv312


Aktivieren:

[Powershell]
.\.venv312\Scripts\Activate.ps1


## 4. Benötigte Bibliotheken installieren

[Powershell]
python -m pip install --upgrade pip
pip install "gymnasium[mujoco]" stable-baselines3 tensorboard


Installierte Pakete:

- Gymnasium – RL-Umgebungen
- MuJoCo – Physiksimulation
- Stable-Baselines3 – RL-Algorithmen (PPO, SAC, TD3)
- TensorBoard – Trainingsvisualisierung

## 5. Ant-Simulation testen

Datei `test_ant.py` im Ordner "ANT_RL_Project" hinzufügen:

Simulation starten:

[Powershell]
python test_ant.py


## 6. Ergebnis

Bei erfolgreicher Ausführung öffnet sich ein MuJoCo-Fenster mit dem vierbeinigen Ant-Roboter.

Der Roboter wird zunächst mit zufälligen Aktionen gesteuert. Ein gezieltes Laufverhalten wird erst durch späteres Reinforcement Learning erlernt.

**Hinweis:** Für dieses Projekt wird Python 3.12 verwendet. Die virtuelle Umgebung muss vor der Ausführung aktiviert sein.