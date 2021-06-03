#!/bin/bash -l
./hybrid -receptor protein_structure.oeb.gz -dbase  compound_library.sdf -hitlist_size 0 -score_file hybrid_score.txt -docked_molecule_file hybrid_docked.sdf.gz -undocked_molecule_file hybrid_undocked.ism.gz -status_file hybrid_status.txt -report_file hybrid_report.txt -settings_file hybrid_settings.txt

