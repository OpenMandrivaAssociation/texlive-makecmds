Name:		texlive-makecmds
Version:	20090903
Release:	1
Summary:	The new \makecommand command always (re)defines a command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makecmds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There
is also \makeenvironment and \provideenvironment for
environments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makecmds/makecmds.sty
%doc %{_texmfdistdir}/doc/latex/makecmds/README
%doc %{_texmfdistdir}/doc/latex/makecmds/makecmds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.dtx
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
