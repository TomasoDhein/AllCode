function AtivarPlataforma(colisao)
  if colisao.Parent:findFirstChild("Humanoid") then
    script.Parent.Transparency = 0
    script.Parent.CanCollide = true
    wait(5)
    DesativarPlatafroma()
  end
end

--=======================================

function DesativarPlatafroma()
  script.Parent.Transparency = 0.5
  script.Parent.CanCollide = false
end

--=======================================

local plataforma = script.Parent
local botao = game.Workspace.Botao
botao.Touched:connect(AtivarPlataforma)
