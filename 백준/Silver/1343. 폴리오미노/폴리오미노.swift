//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/8/24.
//

import Foundation

let n = readLine()!

var parts = n.split(separator: ".", omittingEmptySubsequences: false)

var result = [String]()

for part in parts {
    let count = part.count
    
    if count % 2 != 0 {
        print("-1")
        exit(0)
    }
    
    var temp = ""
    temp += String(repeating: "AAAA", count: count / 4)
    temp += String(repeating: "BB", count: (count % 4) / 2)
        
    result.append(temp)
}

print(result.joined(separator: "."))
