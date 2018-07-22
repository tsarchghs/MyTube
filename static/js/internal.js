const app = new Vue({
  el: '#app',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      isCollapse: true
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }

  }

})
console.log(app)
