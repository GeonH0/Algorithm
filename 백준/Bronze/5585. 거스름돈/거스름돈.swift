//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/10/24.
//

import Foundation

let n = Int(readLine()!)!

var N = 1000-n

let coins = [500,100,50,10,5,1]

var result = 0

for i in coins {
    result += N/i
    N %= i
}

print(result)
