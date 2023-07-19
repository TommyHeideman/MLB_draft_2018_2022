# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:37:57 2023

@author: Tommy
"""
#Tommy Heideman and Joey Matusik 




import mlb_draft_utilities


def main():
    print("MLB DRAFT LAST 5 YEARS\n")
    
    print("HS v COLLEGE\n")
    mlb_draft_utilities.HSvCollege()
    
    print("\nTEAM POSITIONAL DRAFT BREAKDOWN \n")
    mlb_draft_utilities.TeamPosition()
    
    print("\nTOP POSITION DRAFTED\n")
    mlb_draft_utilities.TopPositions()
    
    print("\nTOP 10 SCHOOLS WITH PICKS IN TOP 5 ROUNDS IN PAST 5 DRAFTS\n")
    mlb_draft_utilities.TopSchools()
    

if __name__ == "__main__":
    main()
