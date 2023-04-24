words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    let len = word.lenth
    console.log(word)
    for (let i = 0; i < 6; i ++){
      console.log('word.i : ',i)
      if (word[i] != word[len-i-1]) return 'false';
    }
    // return 'true';

  }
  
for (const word of words) {
  console.log(palindrome(word))
}


// 출력 예시
// true
// true
// true
// false
// false
// false

