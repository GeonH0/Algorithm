//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/7/24.
//

import Foundation
// 분수 찾기

let n = Int(readLine()!)!
var index = 0
var maxValue = 0

while n > maxValue {
    index += 1
    maxValue += index
}

let order = maxValue - n

if index % 2 == 0 {
    print("\(index - order)/\(order + 1)")
} else {
    print("\(order + 1)/\(index - order)")
}
