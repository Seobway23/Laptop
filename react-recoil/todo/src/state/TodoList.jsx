import { atom } from 'recoil';

export const todoListState = atom({
  key: 'TodoList',
  default: [],
});

export const hello = atom({
  key: 'hello',
  default: [],
});
