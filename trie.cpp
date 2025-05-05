#include<iostream>
using namespace std;

class TrieNode {
	public:
	  char data;
	  TrieNode* children[26];
	  bool isTerm;

	  TrieNode(char ch) {
		  data = ch;
		  for (int i = 0 ; i < 26 ; i++) {
			  children[i] = NULL;
		  }
		  is terminal = false;
	  }

};
class Trie {
	public:
	TrieNode* root;
	
	void insertword(string word) {
		edited
