//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/20/24.
//

import Foundation

let N = Int(readLine()!)!

if N % 4 == 0 && (N % 100 != 0 || N % 400 == 0) {
    
    print(1)
    
} else {
    print(0)
}
