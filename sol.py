#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 02:12:19 2022

@author: ccm
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            L = i
            R = i
            while (L >= 0 and R < len(s)):
                
                if (s[L] == s[R]):
                    
                    if ((R-L+1) > resLen):
                        
                        res = s[L : R+1]
                        
                        resLen = R-L+1
                       
                    L = L - 1
                    R = R + 1
                        
                else : 
                    
                    break
                    
        for i in range(len(s)):
            L = i
            R = i + 1
            while (L >= 0 and R < len(s)):
                
                if (s[L] == s[R]):
                    
                    if ((R-L+1) > resLen) :
                        
                        res = s[L : R+1]
                        
                        resLen = R-L+1
                       
                    L = L - 1
                    R = R + 1
                        
                else : 
                    
                    break
                    
        return (res)