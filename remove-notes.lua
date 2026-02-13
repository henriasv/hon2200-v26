-- Remove all Div elements with class "notes"
function Div(el)
  if el.classes:includes("notes") then
    return {}  -- Return empty to remove the element
  end
end
