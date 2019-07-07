import request from '@/utils/request'

export function getTaskList() {
  return request({
    url: '/todos',
    method: 'get',
    headers: { 'content-type': 'application/x-www-form-urlencoded' }
  })
}

export function addTask(data) {
  return request({
    url: '/todos',
    method: 'post',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: data
  })
}
