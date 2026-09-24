# SLE-2: BFS vs DFS Comparison

## Knight's Shortest-Path Problem

This project implements and compares two search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The algorithms are applied to the Knight's Shortest-Path problem on a standard 8×8 chessboard.

## Problem

Given a starting square and a target square, the program finds a sequence of legal Knight moves connecting them.

The starting position is:

- Start: a1
- Goal: h8

## Algorithms

### BFS

Breadth-First Search explores the board level by level and guarantees the shortest path in terms of the number of Knight moves.

### DFS

Depth-First Search explores one branch as deeply as possible before backtracking. It can find a path, but it does not guarantee the shortest path.

## Program Features

The program:

- Implements BFS
- Implements DFS
- Finds a path between two squares
- Counts the number of nodes expanded
- Measures execution time
- Runs each algorithm 5 times
- Displays best, worst, and average execution time

## Requirements

- Python 3.x
- No external libraries are required

## How to Run

Open the terminal in this project folder and run:

```bash
python search_comparison.py