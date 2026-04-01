package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Base domain class from which all other SPDX-3.0 domain classes derive.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Element  {

  private List<ExternalIdentifier> externalIdentifier;
  private List<Extension> extension;
  private String summary;
  private String description;
  private String comment;
  private List<IntegrityMethod> verifiedUsing;
  private List<ExternalRef> externalRef;
  private String name;
  private CreationInfo creationInfo;

}