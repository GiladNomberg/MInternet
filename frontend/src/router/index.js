import Vue from 'vue';
import Router from 'vue-router';
import Todo from '@/components/Todo';
import BarChart from '@/components/BarChart';

Vue.use(Router);
Vue.component(BarChart)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Todo',
      component: Todo,
    },
  ],
  mode: 'history',
});

