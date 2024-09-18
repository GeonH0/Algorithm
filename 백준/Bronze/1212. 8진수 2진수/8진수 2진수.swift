//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/18/24.
//

import Foundation

let N = readLine()!

print(toBinary(N))


func toBinary(_ a: String) -> String {
    var result = ""
    
    for i in a {
        switch i  {
        case "0":
            result += "000"
        case "1":
            result += "001"
        case "2":
            result += "010"
        case "3":
            result += "011"
        case "4":
            result += "100"
        case "5":
            result += "101"
        case "6":
            result += "110"
        case "7":
            result += "111"
        default:
            return result
        }
    }
    
    if let firstNonZeroIndex = result.firstIndex(where: { $0 != "0" }) {
        return String(result[firstNonZeroIndex...])
    } else {
        return "0"
    }
}
