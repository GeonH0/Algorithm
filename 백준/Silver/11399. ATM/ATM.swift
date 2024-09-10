//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/10/24.
//

import Foundation

let N = Int(readLine()!)!

var nums = readLine()!.split(separator: " ").map { Int($0)! }

nums.sort()

var result = 0

for i in 0..<N {
    for j in 0...i {
        result += nums[j]
    }
}

print(result)
