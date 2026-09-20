/** Present events in the same order the API returns them: ascending by version. */
export function presentEvents(events) {
  const list = Array.isArray(events) ? [...events] : []
  list.sort((a, b) => (a.version || 0) - (b.version || 0))
  return list
}

export function presentEventsStable(events) {
  return presentEvents(events)
}
