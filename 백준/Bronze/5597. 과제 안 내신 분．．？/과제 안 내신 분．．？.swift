//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/20/24.
//

import Foundation
var arr = Array(1...30)

var removenumber = Set<Int>()

for _ in 0..<28 {
    var N = Int(readLine()!)!
    removenumber.insert(N)
}
arr = arr.filter { !removenumber.contains($0) }
arr.sort()
for i in arr {
    print(i)
}
