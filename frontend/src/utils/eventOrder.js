/** BUG: newest-first presentation regardless of API. */
export function presentEvents(events) {
  const list = Array.isArray(events) ? [...events] : []
  list.sort((a, b) => (b.version || 0) - (a.version || 0))
  return list
}

export function presentEventsStable(events) {
  return presentEvents(events)
}
