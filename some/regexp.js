// const obj = {
// 	title: 123,
// 	name: 'xioaming',
// 	sex: 1,
// 	second: {
// 		title: 666,
// 		name: 'kangkang',
// 		three: {
// 			sex: 'man'
// 		}
// 	},
// 	age: 78,
// 	Age: 88,
// 	'2BB': 22222,
// 	'1AA': 1212
// }
// // 把对象的键取出来，平铺存进数组里
// function flatObj (obj, key) {
// 	let list = []
//   for (let k in obj) {
//   	let item
//   	if (checkType(obj[k]) === 'object') {
//   		item = (key ? `${key}.` : '') + flatObj(obj[k], k)
//   	} else {
//   		item = (key ? `${key}.` : '') + k
//   	}
//   	item = item.split(',')
//   	Array.prototype.push.apply(list, item)
//   }
//   return list
// }
// const lll = flatObj(obj)
// console.log(lll, 'lll')
// // 检查数据的类型（小写的'string'、'array'、'object'、'null'、'undefined'等等...）
// function checkType (val) {
//   let type = Object.prototype.toString.call(val).replace(/^\[object (.+)\]$/, '$1').toLowerCase();
//   return type
// }
// // 取出对象中某个键的值，键类型为'a.b.c.d'，
// function getVal (obj, key) {
// 	let result
// 	let k = key.split('.')
// 	if (Array.isArray(k)) {
// 		k.reduce((val, item) => {
// 			result = val = val[item]
// 			return val
// 		}, obj)
// 	} else {
// 		result = obj[key]
// 	}
// 	return result
// }
// const vv = getVal (obj, 'second.three.sex')
// console.log(vv, 'vvvv')

