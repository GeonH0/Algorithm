//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 8/25/24.
//

import Foundation

let input = readLine()!
let K = Int(input)!
var nums : [Int] = []

for _ in 1...K {
    
    let num = Int(readLine()!)!
    if num == 0 {
        nums.popLast()
    }
    else {
        nums.append(num)
    }
}

let sum = nums.reduce(0, +)
print(sum)

