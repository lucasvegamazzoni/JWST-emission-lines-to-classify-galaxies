# JWST Galaxy Classification — Emission Line Analysis

## What is this?
Using data from the James Webb Space Telescope (JWST) to classify 
galaxies by analysing their emission lines — the radiation given off 
when ionized gas around stars releases energy.

## The Problem
Different types of galaxies produce different emission line signatures. 
By measuring the ratio of specific emission lines (e.g. Hα, [OIII], [NII]),
we can classify whether a galaxy's energy comes from star formation 
or an active galactic nucleus (AGN).

## My Approach
- Loaded JWST spectral data and extracted emission line flux values
- Computed line ratios to place galaxies on a BPT diagnostic diagram
- Classified galaxies into star-forming, composite, and AGN categories
- Visualised results as scatter plots with classification boundaries

## Tech Stack
Python, matplotlib, numpy, astropy

## Results
See `JWST-emission-lines-to-classify-galaxies.pdf` for sample output showing galaxy classification
on the BPT diagram.
