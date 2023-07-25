function addProjectPathToPythonPath()

prj = currentProject;

for ii = 1:numel(prj.ProjectPath)

    pathii = prj.ProjectPath(ii).File;
    % add to Python path if not there
    if count(py.sys.path, pathii) == 0
        insert(py.sys.path,int32(0), pathii)
    end

end
