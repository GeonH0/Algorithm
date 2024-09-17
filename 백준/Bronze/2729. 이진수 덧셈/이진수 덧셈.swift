import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
    let input = readLine()!.split(separator: " ")
    let a = String(input[0])
    let b = String(input[1])
    
    print(addBinaryStrings(a, b))
}

func addBinaryStrings(_ a: String, _ b: String) -> String {
    var result = ""
    var carry = 0

    var i = a.count - 1
    var j = b.count - 1

    while i >= 0 || j >= 0 || carry > 0 {
        let bitA = i >= 0 ? Int(String(a[a.index(a.startIndex, offsetBy: i)]))! : 0
        let bitB = j >= 0 ? Int(String(b[b.index(b.startIndex, offsetBy: j)]))! : 0

        let sum = bitA + bitB + carry
        let currentDigit = sum % 2
        result = String(currentDigit) + result

        carry = sum / 2

        i -= 1
        j -= 1
    }

    // 앞의 불필요한 '0' 제거
    if let firstNonZeroIndex = result.firstIndex(where: { $0 != "0" }) {
        return String(result[firstNonZeroIndex...])
    } else {
        return "0"
    }
}