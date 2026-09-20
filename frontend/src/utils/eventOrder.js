/** Present events oldest-first: ascending by version, matching the API order. */
export function presentEvents(events) {
  const list = Array.isArray(events) ? [...events] : []
  list.sort((a, b) => (a.version || 0) - (b.version || 0))
  return list
}

export function presentEventsStable(events) {
  return presentEvents(events)
}
