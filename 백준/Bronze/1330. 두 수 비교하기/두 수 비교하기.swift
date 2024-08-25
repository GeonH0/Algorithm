//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 8/25/24.
//

import Foundation

if let input = readLine() {
    let numbers = input.split(separator: " ")
    
    if numbers.count == 2,
       let firstNumber = Int(numbers[0]),
       let secondNumber = Int(numbers[1]) {
        
        if firstNumber > secondNumber {
            print(">")
        } else if firstNumber < secondNumber {
            print("<")
        } else {
            print("==")
        }
    } else {
    
    }
} else {
    
}
